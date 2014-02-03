#from models import *
from bs4 import BeautifulSoup
import sys

def get_tags_from_soup(soup):
    tag = BeautifulSoup('<b></b>')
    tag = tag.b
    tag_list = []
    for foo in soup:
        if type(foo) == type(tag):
            tag_list.append(foo)
    return tag_list

def create_course_from_tag(tag):
    course_name = tag.find('div', {"class":"courseheader"}).text.strip()
    print "course name: [%s]" % course_name
    instructor = tag.find('div', {"class":"coursenotes"}).text.strip()[11:]
    print "instructor: [%s]" % instructor
    textbooks = tag.find('ul').find('div', {"class":"Products"}).table.tbody
    textbooks = get_tags_from_soup(textbooks)
    for book in textbooks:
        title = book.a.text.strip()
        print "title: [%s]" % title
        SKU = book.find('div', id=lambda x: x and
                x.endswith('SKU')).text.strip()[5:]
        print "SKU: [%s]" % SKU 
        prices = book.find('div',
                {"class":"addcartform"}).find('div').findAll('div')
        new_price = float(prices[0].span.text[1:])
        old_price = float(prices[1].span.text[1:])
        print "new_price: [%f]" % new_price
        print "old_price: [%f]" % old_price
    return

def get_course_list_from_soup(soup):
    soup = soup.find(id="ctl00_PageContent_pnlPrintMode")
    return get_tags_from_soup(soup)

def main():
    soup = BeautifulSoup((open(sys.argv[1])))
    print "Opening %s..." % sys.argv[1]
    course_list = get_course_list_from_soup(soup)
    for course in course_list:
        create_course_from_tag(course)
        print ""

if __name__ == "__main__":
        main()
