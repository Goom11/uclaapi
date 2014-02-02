#from models import *
from bs4 import BeautifulSoup
import sys


def single():
    soup = BeautifulSoup(open("/Users/Lowell/gits/uclaapi/scraping/textbooks/single_textbook.html"))

    title = str(soup.tbody.a.text).strip()

    bar = soup.findAll('div', id=lambda x: x and x.endswith('SKU'))
    SKU = str(bar[0].text).strip()[5:]

    textbook = {
        "title": title,
        "SKU": SKU
    }

    print textbook


def multiple():
    soup = BeautifulSoup(open("/Users/Lowell/gits/uclaapi/scraping/textbooks/multiple_textbooks.html"))
    tag = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    tag = tag.b
    course_soup = soup.find(id="ctl00_PageContent_pnlPrintMode")
    courses = []
    for thing in course_soup:
        if type(thing) == type(tag):
            courses.append(thing)
    print "courses:"
    print len(courses)


def create_course_from_tag(tag):
    course_name = tag.find('div', {"class":"courseheader"}).text.strip()
    print "[%s]" % course_name
    instructor = tag.find('div', {"class":"coursenotes"}).text.strip()[11:]
    print "[%s]" % instructor
    return


def get_course_list_from_soup(soup):
    tag = BeautifulSoup('<b></b>')
    tag = tag.b
    soup = soup.find(id="ctl00_PageContent_pnlPrintMode")
    course_list = []
    for foo in soup:
        if type(foo) == type(tag):
            course_list.append(foo)
    return course_list


def main():
    #single()
    #multiple()
    soup = BeautifulSoup((open(sys.argv[1])))
<<<<<<< HEAD
    print "Opening %s..." % sys.argv[1]  
=======
    print "Opening %s..." % sys.argv[1]
    return
>>>>>>> 11af3ad1ed5cdd1d814800027d9e28b8f0a8fc5a
    course_list = get_course_list_from_soup(soup)
    for course in course_list:
        create_course_from_tag(course)


if __name__ == "__main__":
        main()
