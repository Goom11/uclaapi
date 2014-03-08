from pymongo import MongoClient
from pprint import pprint
from bs4 import BeautifulSoup
from models import *
import requests
import urllib
import urllib2
import sys
import re

client = MongoClient()

url = 'http://www.registrar.ucla.edu/catalog/catalog-curricul.htm'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

def get_course_dict(course):
    coursedict = {}
    pprint(course)
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

def get_course_list(max_length = -1):

    course_list = []

    for link in soup.find_all("a", {"class": "main"}):
        coursetitle = link.contents[0]
        intourl = 'http://www.registrar.ucla.edu/catalog/' + link.get('href')
        soup2 = BeautifulSoup(requests.get(intourl).text)
        for link2 in soup2.find_all("a", {"class": "nav-landing-menu"}):
            if 'Course Listings' in link2.contents[0]:
                courseDescriptUrl = 'http://www.registrar.ucla.edu/catalog/' + link2.get('href')
                soup3 = BeautifulSoup(requests.get(courseDescriptUrl).text)
                for link3 in soup3.find_all("p", {"class": "coursebody"}):
                    if type(link3) == type(BeautifulSoup('<b></b>').b):
                        foo = link3
                        course_dict = get_course_dict(foo)
                        course_dict['department'] = link.text.encode('ascii')
                        #pprint(course_dict)
                        course_list.append(course_dict)
                        if max_length > 0 and len(course_list) is max_length:
                            return course_list
    return course_list

def postCourse(course):
    url = "http://127.0.0.1:5000/courses"
    #ugh should do this with a dict comprehension or map or something :/
    course['title'] = course['title'].encode('ascii', 'ignore')
    course['number'] = course['number'].encode('ascii', 'ignore')
    course['description'] = course['description'].encode('ascii', 'ignore')
    data = urllib.urlencode(course)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page

def main():

    length = -1
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    course_list = get_course_list(length)
    print "retrieved %i courses" % len(course_list)
    for course in course_list:
        postCourse(course)
    
if __name__ == "__main__":
    main()
