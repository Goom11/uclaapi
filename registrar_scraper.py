from pymongo import MongoClient
from pprint import pprint
from bs4 import BeautifulSoup
from models import *
import requests
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
    for temp in Temp.objects:
        temp.delete()
        print "deleted %s: %s" % (temp.number, temp.title)

def save_course(coursedict):
    number = coursedict['number']
    description = coursedict['description']
    title = ''
    units = 0
    if 'title' in coursedict:
        title = coursedict['title']
    if 'units' in coursedict:
        units = coursedict['units']
    temp = Temp(number=number, title=title, description=description, units=units)
    temp.save()

def get_course_list():

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
                        #save_course(course_dict)
                        #return
    return course_list

def main():

    clear_db()
    course_list = get_course_list()
    print "retrieved %i courses" % len(course_list)
    
if __name__ == "__main__":
    main()
