from pymongo import MongoClient
import requests
from pprint import pprint
import re
from bs4 import BeautifulSoup

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

def save_course(coursedict):
    return

def main():
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

if __name__ == "__main__":
    main()
