# TODO: use urllib to get HTML
# TODO: scrape HTML into a dict of hours
# TODO: save hours in database (run daily, perhaps get hrs of future dates)
# TODO: wrap with API

import urllib2
from bs4 import BeautifulSoup

def main():
    url = "https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm"
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    table = soup.find('table', {"border":"1"})
    rows = table.findAll('tr')
    date = rows[0].td.strong.text.strip()
    print "date: [%s]" % date
    print rows[1]
    #brkfst, lunch, dinner, late night

if __name__ == "__main__":
    main()
