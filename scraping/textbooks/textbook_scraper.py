from bs4 import BeautifulSoup

def single():
    soup = BeautifulSoup(open("/Users/Lowell/gits/uclaapi/scraping/courses/single_course.html"))
    
    title = str(soup.tbody.a.text).strip()
    
    bar = soup.findAll('div', id=lambda x: x and x.endswith('SKU'))
    SKU = str(bar[0].text).strip()[5:]
    
    course = {
        "title": title,
        "SKU": SKU
    }
    
    print course

def multiple():
    soup = BeautifulSoup(open("/Users/Lowell/gits/uclaapi/scraping/courses/multiple_courses.html"))
    tag = BeautifulSoup('<b class="boldest">Extremely bold</b>')
    tag = tag.b
    course_soup = soup.find(id="ctl00_PageContent_pnlPrintMode")
    courses = []
    for thing in course_soup:
        if type(thing) == type(tag):
            courses.append(thing)
    print "courses:"
    print len(courses)

def main():
    #single()
    multiple()

if __name__ == "__main__":
        main()
