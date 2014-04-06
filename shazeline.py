# COURTESY OF Shahid Chohan
# https://github.com/shazeline

import re
import requests
from bs4 import BeautifulSoup

BASE = 'http://www.registrar.ucla.edu/schedule/'
ID_FILE = 'real_section_ids.txt'

def get_dept_url(term, dept):
  return BASE + 'crsredir.aspx?termsel=%s&subareasel=%s' % (term, dept)

def get_course_url(term, dept, id):
  return BASE + 'detselect.aspx?termsel=%s&subareasel=%s&idxcrs=%s' % (term, dept, id)

def get_soup(url):
  response = requests.get(url)
  return BeautifulSoup(response.text)

def get_values(soup):
  return [option.get('value') for option in soup.find_all('option')]

def get_all_course_urls(term, dept, dept_url):
  soup = get_soup(dept_url)
  course_ids = get_values(soup)
  return [get_course_url(term, dept, course_id) for course_id in course_ids]

def cell_text(cell):
  return ' '.join(cell.stripped_strings)

def parse_table(table):
  data = []
  for row in table.find_all('tr'):
    row_data = map(cell_text, row.find_all(re.compile('t[dh]')))[::2]
    data.append(row_data)
  return data

def get_IDs(course_url):
  soup = get_soup(course_url)
  matches = soup.find_all(class_='dgdClassDataColumnIDNumber')
  raw_urls = [str(match) for match in matches if 'bold' in str(match) and '?srs=' in str(match)]
  ids = []
  # put regex here later
  for link in raw_urls:
    equals_index = link.find('?srs=')
    id = link[equals_index+5:equals_index+14]
    ids.append(id)
  return ids

def get_course_status(course_url):
  tables = soup.find_all('table')
  if len(tables) < 8:
    return
  enrollment_table = tables[8]
  enrollment_data = parse_table(enrollment_table)
  for row in range(1, len(enrollment_data)):
    print enrollment_data[row][1] + ' ' + \
          enrollment_data[row][2] + ':\t' + \
          enrollment_data[row][13]
  print '======================='

def get_course_url_list():
  soup = get_soup(BASE + 'schedulehome.aspx')
  values = get_values(soup)
  terms = values[0:4]
  depts = values[4:]
  spring = terms[0]
  dept_urls = [get_dept_url(spring, dept) for dept in depts]
  all_urls = []
  for i, dept_url in enumerate(dept_urls):
    course_urls = get_all_course_urls(spring, depts[i], dept_url)
    all_urls += course_urls
  return all_urls

def print_ids_to_file():
  course_urls = get_course_url_list()
  all_ids = []
  for course_url in course_urls:
    print course_url
    IDs = get_IDs(course_url)
    for ID in IDs:
      if ID is not None:
        print "adding %r" % ID
        all_ids.append(ID)

    f = open(ID_FILE, 'w')
    for ID in all_ids:
        print "writing %r" % ID
        f.write('%s\n' % ID)
    f.close

def main():
    print_ids_to_file()

if __name__ == "__main__":
    main()
