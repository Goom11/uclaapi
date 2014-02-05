from models import *
from bs4 import BeautifulSoup
from pprint import pprint
import sys

# TODO : implement save method

def get_tags_from_soup(soup):
    tag = BeautifulSoup('<b></b>')
    tag = tag.b
    tag_list = []
    for foo in soup:
        if type(foo) == type(tag):
            tag_list.append(foo)
    return tag_list

def save_course(course_dict):
    course = Course(name=course_dict['course_name'], instructor=course_dict['instructor'])
    course.save()
    for book in course_dict['books']:
        print book
        textbook = Textbook(title=book['title'], SKU=book['SKU'])
        if 'used_price' in course_dict:
            textbook.used_price = book['used_price']
        if 'new_price' in course_dict:
            textbook.new_price = book['new_price']
        textbook.save() 
    return

def create_coursedict_from_tag(tag):
    coursedict = {}
    coursedict['course_name'] = tag.find('div', {"class":"courseheader"}).text.strip()
    coursedict['instructor'] = str(tag.find('div',
        {"class":"coursenotes"}).text.strip()[11:])
    coursedict['books'] = []
    try:
        textbooks = tag.find('ul').find('div', {"class":"Products"}).table.tbody
        textbooks = get_tags_from_soup(textbooks)
        for book in textbooks:
            bookdict = {}
            bookdict['title'] = str(book.a.text.strip())
            bookdict['SKU'] = str(book.find('div', id=lambda x: x and
                    x.endswith('SKU')).text.strip()[5:])
            prices = book.find('div',
                    {"class":"addcartform"}).find('div').findAll('div')

            for price in prices:
                ch = price.get_text().strip()[0]
                if ch == 'N':
                    bookdict['new_price'] = float(price.span.text[1:])
                elif ch == 'U':
                    bookdict['used_price'] = float(price.span.text[1:])

            coursedict['books'].append(bookdict)
    except AttributeError:
        print "no textbooks found for %r" % coursedict
    return coursedict

def get_course_list_from_soup(soup):
    soup = soup.find(id="ctl00_PageContent_pnlPrintMode")
    return get_tags_from_soup(soup)

def main():
    soup = BeautifulSoup((open(sys.argv[1])))
    course_list = get_course_list_from_soup(soup)
    for course in course_list:
        #print ""
        save_course(create_coursedict_from_tag(course))
    #print ""

if __name__ == "__main__":
        main()

