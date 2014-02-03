# TODO: use urllib to get HTML
# TODO: scrape HTML into a dict of hours
# TODO: save hours in database (run daily, perhaps get hrs of future dates)
# TODO: wrap with API

import urllib2
from pprint import pprint
from bs4 import BeautifulSoup

def plain_text(strong_tag):
    try:
        return str(strong_tag.strong.text.strip())
    except AttributeError:
        return strong_tag

def main():
    url = "https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm"
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    table = soup.find('table', {"border":"1"})
    rows = table.findAll('tr')
    hourdict = {}
    hourdict['date'] = plain_text(rows[0].td)
    hourdict['restaurants'] = []
    for i in range(2,10):
        cells = rows[i].findAll('td')
        restaurantdict = {}
        restaurantdict['name'] = plain_text(cells[0])
        restaurantdict['hours'] = {}

        breakfast = cells[1].findAll('strong')
        lunch     = cells[2].findAll('strong')
        dinner    = cells[3].findAll('strong')
        latenight = cells[4].findAll('strong')

        #print breakfast

        periods = ['breakfast', 'lunch', 'dinner', 'late night']

        for i, period in enumerate(periods):
            hours = cells[i+1].findAll('strong')
            restaurantdict['hours'][period] = {}
            restaurantdict['hours'][period]['open'] = plain_text(hours[0])
            restaurantdict['hours'][period]['close'] = plain_text(hours[1])
            break

        hourdict['restaurants'].append(restaurantdict)
        break
    pprint(hourdict)

if __name__ == "__main__":
    main()
