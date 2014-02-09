# TODO: save hours in database (run daily, perhaps get hrs of future dates)
# TODO: wrap with API

import urllib2
from pprint import pprint
from bs4 import BeautifulSoup

def no_slash(date):
    #return time.split()[0]
    output = ""
    for i in range(len(date)):
        if date[i] == ' ':
            return output
        else:
            output += date[i]

def plain_text(strong_tag):
    return str(strong_tag.get_text().strip())

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

        periods = ['breakfast', 'lunch', 'dinner', 'late night']

        for i, period in enumerate(periods):
            hours = cells[i+1].findAll('strong')
            restaurantdict['hours'][period] = {}
            if len(hours) == 1:
                restaurantdict['hours'][period]['close'] = 'CLOSED'
                restaurantdict['hours'][period]['open'] = 'CLOSED'
            else:
                restaurantdict['hours'][period]['close'] = plain_text(hours[1])
                restaurantdict['hours'][period]['open'] = no_slash(plain_text(hours[0]))

        hourdict['restaurants'].append(restaurantdict)
    pprint(hourdict)

if __name__ == "__main__":
    main()
