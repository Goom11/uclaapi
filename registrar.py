from pymongo import MongoClient
from pprint import pprint
from bs4 import BeautifulSoup
from models import *
import requests
import sys
import re

client = MongoClient()

url = 'http://www.registrar.ucla.edu/catalog/catalog-curricul.htm'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

def get_course_dict(course):
    coursedict = {}
    title = course.span.text.strip()
    words = title.split('.')
    coursedict['number'] = words[0].strip()
    try:
        coursedict['title'] = ''.join(words[1:-1]).strip()
        coursedict['units'] = int(re.findall('\d+', words[-1])[0])
        # TODO: accomodate possible unit ranges (e.g. 2-8)
    except IndexError:
        # TODO: accomodate this
        print "course %r is not formatted correctly" % title
    coursedict['description'] = course.get_text().split('\n')[-1]
    return coursedict

def clear_db():
    #clear the database to prevent against pk errors
    for course in Course.objects:
        course.delete()
        print "deleted %s: %s" % (course.number, course.title)

def save_course(coursedict):
    number = coursedict['number']
    description = coursedict['description']
    title = ''
    units = 0
    if 'title' in coursedict:
        title = coursedict['title']
    if 'units' in coursedict:
        units = coursedict['units']
    
    # fuck it, it's a hackathon
    department = "DEPT"
    quarter = "QTR"
    instructor = "PROF"

    course = Course(number=number, title=title, description=description, units=units, department=department, quarter=quarter, instructor=instructor)
    #course = Course(number=number, title=title, description=description, units=units)
    course.save()
    # temp = Temp(number=number, title=title, description=description, units=units)
    # temp.save()
    print "SAVED %s ..." % description[:50]

def get_course_list(max_length = -1):

    course_list = []

    for link in soup.find_all("a", {"class": "main"}):
        coursetitle = link.contents[0]
        intourl = 'http://www.registrar.ucla.edu/catalog/' + link.get('href')
        # print(url + "/" + link.get('href') + "\n" + coursetitle)
        soup2 = BeautifulSoup(requests.get(intourl).text)
        for link2 in soup2.find_all("a", {"class": "nav-landing-menu"}):
            if 'Course Listings' in link2.contents[0]:
                courseDescriptUrl = 'http://www.registrar.ucla.edu/catalog/' + link2.get('href')
                soup3 = BeautifulSoup(requests.get(courseDescriptUrl).text)
                for link3 in soup3.find_all("p", {"class": "coursebody"}):
                    if type(link3) == type(BeautifulSoup('<b></b>').b):
                        foo = link3
                        course_dict = get_course_dict(foo)
                        pprint(course_dict)
                        course_list.append(course_dict)
                        if max_length > 0 and len(course_list) is max_length:
                            return course_list
    return course_list

def main():

    clear_db()
    length = -1
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    course_list = get_course_list(length)
    print "retrieved %i courses" % len(course_list)
    for course in course_list:
        save_course(course)
    
if __name__ == "__main__":
    main()
