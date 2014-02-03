#from models import *
from bs4 import BeautifulSoup
from pprint import pprint
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
    coursedict = {}
    coursedict['course_name'] = tag.find('div', {"class":"courseheader"}).text.strip()
    coursedict['instructor'] = str(tag.find('div',
        {"class":"coursenotes"}).text.strip()[11:])
    coursedict['books'] = []
    textbooks = tag.find('ul').find('div', {"class":"Products"}).table.tbody
    textbooks = get_tags_from_soup(textbooks)
    for book in textbooks:
        bookdict = {}
        bookdict['title'] = str(book.a.text.strip())
        bookdict['SKU'] = str(book.find('div', id=lambda x: x and
                x.endswith('SKU')).text.strip()[5:])
        prices = book.find('div',
                {"class":"addcartform"}).find('div').findAll('div')
        bookdict['new_price'] = float(prices[0].span.text[1:])
        bookdict['old_price'] = float(prices[1].span.text[1:])
        coursedict['books'].append(bookdict)
    pprint(coursedict)
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

