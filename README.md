uclaapi
=======

Making it easier for students to create UCLA-related apps.

Using [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Flask-MongoEngine](https://flask-mongoengine.readthedocs.org/en/latest/).

give it a try!
=======

To generate JSON from the [dining hours](https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm) webpage,
````
$ python dining_hours_scraper.py

# {'date': 'Monday, February 03',
#  'restaurants': [{'hours': {'breakfast': {'close': '11:00am',
#                                           'open': '7:00am'},
#                             'dinner': {'close': '9:00pm', 'open': '5:00pm'},
#                             'late night': {'close': '2:00am',
#                                            'open': '9:00pm'},
#                             'lunch': {'close': '5:00pm', 'open': '11:00am'}},
#                   'name': 'Bruin Cafe'},
#     ... 

````

To generate JSON from the [textbook store](http://shop.uclastore.com/courselistbuilder.aspx),
````
$ python textbook_scraper.py textbook_html/moar_txtbks.html #or multiple_textbooks.html, single_textbook.html

# {'books': [{'SKU': '9780131749207',
#             'new_price': 35.75,
#             'title': 'TOP NOTCH 1 WITH SUPER CD-ROM',
#             'used_price': 27.0},
#            {'SKU': '9780131997301',
#             'new_price': 35.75,
#             'title': 'TOP NOTCH FUNDAMENTALS W/ SUPER CD-ROM',
#             'used_price': 27.0}],
#  'course_name': u'Winter 2014 - UCLA - ALC 945\xa0- Section\xa02',
#  'instructor': 'NEUWIRTH'}
#     ... 
````

TODO
=======

* ~~Scrape the [textbook store](http://shop.uclastore.com/courselistbuilder.aspx)~~ DONE!
* ~~Scrape [dining hours](https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm)~~ DONE!
* Scrape [dining menus](http://menu.ha.ucla.edu/foodpro/default.asp)
* Scrape the [Registrar](http://www.registrar.ucla.edu/catalog/catalog-curricul.htm)
* Sexy versions of all of these
