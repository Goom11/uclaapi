uclaapi
=======

Fostering the UCLA app ecosystem.

getting started
==================================

```
git clone https://github.com/Goom11/uclaapi.git
cd uclaapi
pip install virtualenv
virtualenv --distribute venvucla
source venvucla/bin/activate
pip install -r requirements.txt
```

give it a try!
==============

To populate and run the registar API server,
````
# if for any command you receive an ImportError, be sure that you've sourced the virtual environment
$ mongod              # in another window
$ python run.py       # in another window
$ python registrar.py # this will populate the database and will take a minute or so
````
Go to [http://localhost:5000/courses](http://localhost:5000/courses) to enjoy the fruits of your labor! We reccomend using [Postman](https://chrome.google.com/webstore/detail/postman-rest-client-packa/fhbjgbiflinjbdggehcddcbncdddomop) to interact with this RESTful API.

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

* Scrape the [textbook store](http://shop.uclastore.com/courselistbuilder.aspx)
* Scrape [dining hours](https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm)
* Scrape [dining menus](http://menu.ha.ucla.edu/foodpro/default.asp)
* Scrape the [Registrar](http://www.registrar.ucla.edu/catalog/catalog-curricul.htm)
* Scrape [library hours](http://www.library.ucla.edu/about/hours)
* midterm/final/homework/quiz/lectureSlides/notes/cheatSheet/studyGuide BANK
