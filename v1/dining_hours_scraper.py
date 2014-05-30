# TODO: save hours in database (run daily, perhaps get hrs of future dates)
# TODO: wrap with API

import urllib2
import dateutil.parser
from pprint import pprint
from models import *
from bs4 import BeautifulSoup

def no_slash(time):
    return time.split()[0]

def plain_text(strong_tag):
    return str(strong_tag.get_text().strip())

def get_html(source):
    if source == 'local':
        return open(sys.argv[1])
    else:
        url = "https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm"
        response = urllib2.urlopen(url)
        html = response.read()
        return html

def get_dining_dict():
    html = get_html('')
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
    return hourdict

# should be using:
# http://docs.mongoengine.org/en/latest/guide/querying.html#atomic-updates
def get_or_create_restaurant(name):
    restaurant = Restaurant.objects(name=name).first()
    # ^ sketch. should error log if returns more than a single object?
    if restaurant is None:
        restaurant = Restaurant(name=name)
        restaurant.save()
        print "created new Restaurant object: %s" % restaurant.name
    # return the existing or newly created restaurant object
    return restaurant

def find_hour(hours, name, date):
    # for hour in hours:
    #     if hour.name == name:
    return None

# TODO: impelement this to prevent duplicates:
# def get_or_create_hour(restaurant, name, date):
#     hours = 

def save_dict(dictionary):
    # pprint(dictionary)
    date = dictionary['date']
    #TODO: conflate breakfast and lunch if they are the same (brunch)
    for resto in dictionary['restaurants']:
        name = resto['name']
        restaurant = get_or_create_restaurant(name=name)
        # pprint(resto)
        for period in resto['hours']:
            # print "%s : %r" % (period, resto['hours'][period])
            start = date + ' ' +  resto['hours'][period]['open'] 
            start = dateutil.parser.parse(start)
            end = date + ' ' +  resto['hours'][period]['close'] 
            end = dateutil.parser.parse(end)
            print start
            print end
            hour = Hour(name=period, start=start, end=end)
            hour.save()
            restaurant.hours.append(hour)

def main():
    dictionary = get_dining_dict()
    save_dict(dictionary)

if __name__ == "__main__":
    main()
