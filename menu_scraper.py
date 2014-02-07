import urllib2
from pprint import pprint
from bs4 import BeautifulSoup


def left_and_right(table):
    left = {}
    right = {}
    for tr in table.findAll('tr'):
        tds = tr.findAll('td')

def main():
    print "hello world"
    url = "http://menu.ha.ucla.edu/foodpro/default.asp"
    # there's a more complete listing at:
    # http://menu.ha.ucla.edu/foodpro/default.asp?date=2%2F6%2F2014&meal=2&threshold=2
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    tables = soup.findAll('table', {"class":"menugridtable"})
    # 0 = Covel, De Neve; 2 = Feast, B-Plate
    lunchmenus = tables[:2] 
    dinnermenus = tables[2:]

if __name__ == "__main__":
    main()
