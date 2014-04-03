# COURTESY OF Shahid Chohan
# https://github.com/shazeline

import re
import requests
from bs4 import BeautifulSoup

BASE = 'http://www.registrar.ucla.edu/schedule/'

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

def get_course_status(course_url):
  soup = get_soup(course_url)
  tables = soup.find_all('table')
  if len(tables) < 8:
    return
  enrollment_table = tables[8]
  enrollment_data = parse_table(enrollment_table)
  print course_url
  for row in range(1, len(enrollment_data)):
    print enrollment_data[row][1] + ' ' + \
          enrollment_data[row][2] + ':\t' + \
          enrollment_data[row][13]
  print '======================='

def main():
    soup = get_soup(BASE + 'schedulehome.aspx')
    values = get_values(soup)
    terms = values[0:4]
    depts = values[4:]
    spring = terms[0]
    dept_urls = [get_dept_url(spring, dept) for dept in depts]
    
    for i, dept_url in enumerate(dept_urls):
      course_urls = get_all_course_urls(spring, depts[i], dept_url)
      for course_url in course_urls:
        get_course_status(course_url)

if __name__ == "__main__":
    main()
