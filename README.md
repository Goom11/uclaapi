uclaapi
=======

Making it easier for students to create UCLA-related apps.

Using [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Flask-MongoEngine](https://flask-mongoengine.readthedocs.org/en/latest/)

give it a try!
=======

To generate JSON from the [dining hours](https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm) webpage,
````
$ python dining_hours_scraper.py
````

To generate JSON from the [textbook store](http://shop.uclastore.com/courselistbuilder.aspx),
````
$ python textbook_scraper.pytextbook_html/moar_txtbks.html #or multiple_textbooks.html, single_textbook.html
````

TODO
=======

* ~~Scrape the [textbook store](http://shop.uclastore.com/courselistbuilder.aspx)~~ DONE!
* ~~Scrape [dining hours](https://secure5.ha.ucla.edu/restauranthours/dining-hall-hours-by-day.cfm)~~ DONE!
* Scrape [dining menus](http://menu.ha.ucla.edu/foodpro/default.asp)
* Scrape the Registrar
