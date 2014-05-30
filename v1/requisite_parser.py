import requests
from bs4 import BeautifulSoup

# TODO(Shahid) - How do you parse this shit? Fix L/R associativity rules perhaps?
  # http://www.registrar.ucla.edu/schedule/subdet.aspx?srs=145744200&term=14S

# TODO(Shahid) - Look into whether reverse dict is more in practice.
dept_map = {'AERO ST':'Aerospace Studies',
            'AF LANG':'African Languages',
            'AFRC ST':'African Studies',
            'AFRKAAN':'Afrikaans',
            'AFRO-AM':'Afro-American Studies',
            'AM IND':'American Indian Studies',
            'ASL':'American Sign Language',
            'AN N EA':'Ancient Near East',
            'ANTHRO':'Anthropology',
            'APPLING':'Applied Linguistics',
            'ARABIC':'Arabic',
            'ARCHEOL':'Archaeology',
            'ARCH&UD':'Architecture and Urban Design',
            'ARMENIA':'Armenian',
            'ART':'Art',
            'ART HIS':'Art History',
            'ART&ARC':'Arts and Architecture',
            'ASIAN':'Asian',
            'ASIA AM':'Asian American Studies',
            'ASTR':'Astronomy',
            'A&O SCI':'Atmospheric and Oceanic Sciences ',
            'BERBER':'Berber',
            'BIOENGR':'Bioengineering',
            'BIOINFO':'Bioinformatics (Graduate)',
            'BIOINFR':'Bioinformatics (Undergraduate)',
            'BIOL CH':'Biological Chemistry',
            'BIOMATH':'Biomathematics',
            'BMEDPHY':'Biomedical Physics',
            'BMD RES':'Biomedical Research',
            'BIOSTAT':'Biostatistics',
            'BULGAR':'Bulgarian',
            'CEE STD':'Central and East European Studies ',
            'CH ENGR':'Chemical Engineering',
            'CHEM':'Chemistry and Biochemistry',
            'CHICANO':'Chicana and Chicano Studies',
            'CHIN':'Chinese',
            'CIVIC':'Civic Engagement',
            'C&EE':'Civil and Environmental Engineering',
            'CLASSIC':'Classics',
            'COMM ST':'Communication Studies',
            'COM HLT':'Community Health Sciences',
            'COM LIT':'Comparative Literature',
            'C&S BIO':'Computational and Systems Biology',
            'COM SCI':'Computer Science',
            'CAEM':'Conservation of Archaeological Ethnographi...',
            'CZECH':'Czech',
            'DANCE':'Dance',
            'DENT':'Dentistry',
            'DESMA':'Design | Media Arts',
            'DGT HUM':'Digital Humanities',
            'DIS STD':'Disability Studies',
            'DUTCH':'Dutch',
            'E&S SCI':'Earth and Space Sciences (Pre-Winter 2014)',
            'EPS SCI':'Earth, Planetary, and Space Sciences',
            'EA STDS':'East Asian Studies',
            'E A STD':'East Asian Studies (Pre Fall 2012)',
            'EE BIOL':'Ecology and Evolutionary Biology ',
            'ECON':'Economics',
            'EDUC':'Education',
            'EL ENGR':'Electrical Engineering',
            'ENGR':'Engineering',
            'ENGL':'English',
            'ESL':'English as a Second Language ',
            'ENGCOMP':'English Composition',
            'ENVIRON':'Environment',
            'ENV HLT':'Environmental Health Sciences',
            'EPIDEM':'Epidemiology',
            'ETHNOMU':'Ethnomusicology',
            'FAM MED':'Family Medicine',
            'FILIPNO':'Filipino',
            'FILM TV':'Film and Television',
            'FRNCH':'French',
            'GENDER':'Gender Studies',
            'GE CLST':'General Education Clusters',
            'GEOG':'Geography',
            'GERMAN':'German',
            'GRNTLGY':'Gerontology',
            'GLBL ST':'Global Studies',
            'GREEK':'Greek',
            'HLT POL':'Health Policy and Management',
            'HEBREW':'Hebrew',
            'HIN-URD':'Hindi-Urdu',
            'HIST':'History',
            'HNRS':'Honors Collegium',
            'HUM GEN':'Human Genetics',
            'HUNGRN':'Hungarian',
            'ILA':'Indigenous Languages of the Americas',
            'I E STD':'Indo-European Studies',
            'INDO':'Indonesian',
            'INF STD':'Information Studies',
            'I A STD':'International and Area Studies',
            'INTL DV':'International Development Studies',
            'IRANIAN':'Iranian',
            'ISLAMIC':'Islamics',
            'ISLM ST':'Islamic Studies',
            'ITALIAN':'Italian',
            'JAPAN':'Japanese',
            'JEWISH':'Jewish Studies',
            'KOREA':'Korean',
            'LBR&WS':'Labor and Workplace Studies',
            'LATIN':'Latin',
            'LATN AM':'Latin American Studies',
            'LAW':'Law',
            'UG-LAW':'Law, Undergraduate',
            'LGBTS':'Lesbian, Gay, Bisexual, and Transgender St...',
            'LIFESCI':'Life Sciences',
            'LING':'Linguistics',
            'LITHUAN':'Lithuanian',
            'MGMT':'Management',
            'MAT SCI':'Materials Science and Engineering',
            'MATH':'Mathematics',
            'MECH&AE':'Mechanical and Aerospace Engineering',
            'MED HIS':'Medical History',
            'MED':'Medicine',
            'MIMG':'Microbiology, Immunology, and Molecular Ge...',
            'M E STD':'Middle Eastern Studies',
            'MIL SCI':'Military Science',
            'M PHARM':'Molecular and Medical Pharmacology',
            'MOL BIO':'Molecular Biology',
            'MCD BIO':'Molecular, Cell, and Developmental Biology',
            'MC&IP':'Molecular, Cellular, and Integrative Physi...',
            'MOL TOX':'Molecular Toxicology',
            'MIA STD':'Moving Image Archive Studies',
            'MUSIC':'Music',
            'MUS HST':'Music History',
            'MUS IND':'Music Industry',
            'MUSCLGY':'Musicology',
            'NAV SCI':'Naval Science',
            'NR EAST':'Near Eastern Languages',
            'NEURBIO':'Neurobiology',
            'NEURLGY':'Neurology',
            'NEUROSC':'Neuroscience',
            'NEURO':'Neuroscience (Graduate)',
            'NEURSGY':'Neurosurgery',
            'NURSING':'Nursing',
            'OBGYN':'Obstetrics and Gynecology',
            'OPTH':'Opthalmology',
            'ORL BIO':'Oral Biology',
            'ORTHPDC':'Orthopaedic Surgery',
            'PATH':'Pathology and Laboratory Medicine',
            'PEDS':'Pediatrics',
            'PHILOS':'Philosophy',
            'PHYSICS':'Physics',
            'PHYSCI':'Physiological Science',
            'PHYSIOL':'Physiology',
            'POLISH':'Polish',
            'POL SCI':'Political Science',
            'PORTGSE':'Portuguese',
            'COMPTNG':'Program in Computing',
            'PSYCTRY':'Psychiatry and Biobehavioral Sciences',
            'PSYCH':'Psychology',
            'PUB HLT':'Public Health',
            'PUB PLC':'Public Policy',
            'RAD ONC':'Radiation Oncology',
            'RELIGN':'Religion, Study of',
            'ROMAN':'Romanian',
            'RUSSIAN':'Russian',
            'SCAND':'Scandinavian',
            'SCI EDU':'Science Education',
            'SEMITIC':'Semitics',
            'SER CRO':'Serbian/Croatian',
            'SLAVIC':'Slavic',
            'SOC THT':'Social Thought',
            'SOC WLF':'Social Welfare',
            'SOC GEN':'Society and Genetics',
            'SOCIOL':'Sociology',
            'S ASIAN':'South Asian',
            'SEASIAN':'Southeast Asian',
            'SPAN':'Spanish',
            'STATS':'Statistics',
            'SURGERY':'Surgery',
            'THAI':'Thai',
            'THEATER':'Theater',
            'TURKIC':'Turkic Languages',
            'UKRAIN':'Ukrainian',
            'URBN PL':'Urban Planning',
            'UROLOGY':'Urology',
            'VIETMSE':'Vietnamese',
            'WL ARTS':'World Arts and Cultures',
            'YIDDSH':'Yiddish'}

course_name_class = 'coursehead'
enforced_requisites_id = 'ctl00_BodyContentPlaceHolder_subdet_lblEnforcedReq'

def get_raw_requisites_data(url):
  """Get the raw "enforced requisites" string from a given URL"""
  response = requests.get(url)
  if response.status_code != 200:
    raise Exception('Error while making GET request: %s' % response.status_code)

  soup = BeautifulSoup(response.text)

  course_name = soup.find('span', course_name_class).text
  course_name = course_name.split('.')[0]
  course_name = ' '.join(course_name.split())
  course_data = course_name.split(' ')
  course_num  = course_data[:-1]
  course_dept = ' '.join(course_data[0:len(course_data)-1])
  course_dept = dept_map.get(course_dept, course_dept)

  course_requisites = soup.find('span', {'id': enforced_requisites_id}).text
  return course_requisites, course_dept

def string_is_course_id(string):
  """
  A string is an ID if any of the first 3 characters are digits

  e.g.
  111   -> True
  M152a -> True
  CM102 -> True
  Computer Science 111 -> False
  """
  for i in range(min(len(string), 3)):
    if string[i].isdigit():
      return True
  return False

# TODO(Shahid) - Modularize this.
def get_requisites(url):
  """
  Returns a list of list of courses that are requisites of the course at the given url.
  Requisite logic is in conjunctive normal form.

  e.g.
  raw string: courses (103 or C125) and (106 or C115) and 108A and Computer Science 31
  result:     [
                [u'Chemical Engineering 103', u'Chemical Engineering C125'],
                [u'Chemical Engineering 106', u'Chemical Engineering C115'],
                [u'Chemical Engineering 108A'],
                [u'Computer Science 31']
              ]
  """
  course_requisites, course_dept = get_raw_requisites_data(url)
  if course_requisites == 'None':
    return []

  # Order matters!
  bad_strings = ['(', ')', 'C- or better', 'corequisite', 'courses', 'course']
  for bad_string in bad_strings:
    course_requisites = course_requisites.replace(bad_string, '').strip()

  course_requisites = course_requisites.split(' and ')
  fixed_requisites = [requisite.split(' or ') for requisite in course_requisites]

  depts = []
  for req_list in fixed_requisites:
    course_name = req_list[0]
    if string_is_course_id(course_name):
      depts.append(course_dept)
    else:
      data = course_name.split(' ')
      dept = ' '.join(data[0:len(data)-1])
      depts.append(dept)

  for i, req_list in enumerate(fixed_requisites):
    for j, course in enumerate(req_list):
      if string_is_course_id(course):
        fixed_name = depts[i] + ' ' + course
        req_list[j] = fixed_name
        fixed_requisites[i] = req_list

  return fixed_requisites

# Good example
def parse_example():
  url = 'http://www.registrar.ucla.edu/schedule/subdet.aspx?srs=369349200&term=14s'
  print get_requisites(url)

# parse_example()