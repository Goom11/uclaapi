from uclaapi import db

###### Textbooks/Registrar ###### 

class Textbook(db.Document):
   title = db.StringField(max_length=255, required=True)
   SKU = db.StringField(max_length=255, required=True)
   new_price = db.DecimalField(min_value=0)
   used_price = db.DecimalField(min_value=0)

# this object is getting heavy, but projection should take care of that
class Course(db.Document):
   # TODO: parse 'name' to separate fields!
   name = db.StringField(max_length=255, required=True, unique=True)
   description = db.StringField(required=True)
   department = db.StringField(max_length=255, required=True, unique=True) #eg Math
   number = db.StringField(max_length=255, required=True, unique=True) #eg 33A
   quarter = db.StringField(max_length=255, required=True, unique=True) #eg Winter
   year = db.DecimalField(min_value=0) #eg 2014
   # TODO: move instructor to lecture
   instructor = db.StringField(max_length=255, required=True, unique=True)
   books = db.ListField(db.ReferenceField(Textbook))
   prerequisites = db.ListField(db.ReferenceField(Course))

class Lecture(db.Document): # subclasses Course, has specific instructor & classroom number?
   number = db.StringField(max_length=255, required=True, unique=True) #eg 3
   professor = db.ReferenceField(Instructor)

class Section(db.Document): # subclasses Lecture, has specific TA & classroom number
   section = db.StringField(max_length=255, required=True, unique=True) #eg C
   ta = db.ReferenceField(Instructor)

class Instructor(db.Document):
   first_name = db.StringField(max_length=255)
   last_name = db.StringField(max_length=255, required=True) #can't be unique b/c multiple profs with same same, so there needs to be some alternative pk
   #type = ta|professor # stringfield doesn't seem concrete enough. can we create a data type that only has two values? boolean? what if we want three later on?

###### Dining ###### 

class Restaurant(db.Document)
   name = db.StringField(max_length=255, required=True, unique=True)
   Menus = db.ListField(db.ReferenceField(Menu))
   #Hours = 

class Menu(db.Document):
   date = db.DateTimeField(required=True) 
   foods = db.ListField(db.ReferenceField(Food))

class Food(db.Document):
   name = db.StringField(max_length=255, required=True, unique=True)
   ingredients = db.ListField(db.StringField(max_length=255))

class Hours(db.Document):
   date = db.DateTimeField(required=True) 
   # some fancy way to handle varying meal periods and breaks within meal periods
   # would be cool to use this same model for Library?
   # this data is going to be repeated a lot though.
   # perhaps other models should point to this model instead of creating a new
   # one if this one alreadt exists?
   # for this model to be useful to meal periods, the relation between meal
   # periods and and Hours should be bijective? right? because that would allow
   # for this to be a heurisitic of how many swipes you can use before the
   # week's over?
   # then there are things like the library hours which have different hours for
   # different parts of the library. :/

# unsorted models

class Building(db.Document):
    # amenities like room reservations! programatically send emails to reserve rooms lol. 

class Library(db.Document):
    #hours
