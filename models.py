# TODO: sane defaults for all fields

from uclaapi import db

###### Textbooks/Registrar ###### 

class Textbook(db.Document):
    title = db.StringField(max_length=255, required=True)
    SKU = db.StringField(max_length=255, required=True)
    new_price = db.DecimalField(min_value=0)
    used_price = db.DecimalField(min_value=0)

class Instructor(db.Document):
   first_name = db.StringField(max_length=255)
   last_name = db.StringField(max_length=255, required=True) 
   # last_name can't be unique b/c multiple profs with same same, 
   # so there needs to be some alternative pk
   # type = ta|professor # stringfield doesn't seem concrete enough. can we create a data type that only has two values? boolean? what if we want three later on?

class Course(db.Document):
    # TODO: parse 'name' to separate fields!
    name = db.StringField(max_length=255, required=True, unique=True)
    description = db.StringField(required=True)
    department = db.StringField(max_length=255, required=True, unique=True) 
    number = db.StringField(max_length=255, required=True, unique=True)
    quarter = db.StringField(max_length=255, required=True, unique=True) 
    year = db.DecimalField(min_value=0) 
    # TODO: move instructor to lecture
    instructor = db.StringField(max_length=255, required=True, unique=True)
    books = db.ListField(db.ReferenceField(Textbook))
    #prerequisites = db.ListField(db.ReferenceField(Course))
    units = db.DecimalField(min_value=0)
    # grading detail, GE status, impacted class, enrollment restriction, 

class Room(db.Document):
    number = db.StringField(max_length=255, required=True, unique=True) 
    max_occupancy = db.IntField(min_value=0)
    # svg layover

class Hour(db.Document):
    name = db.StringField(max_length=255, required=True, unique=True)
    start = db.DateTimeField(required=True) 
    end = db.DateTimeField(required=True) 

class Section(db.Document): 
   letter = db.StringField(max_length=255, required=True, unique=True)
   ta = db.ReferenceField(Instructor)
   location = db.ReferenceField(Room)
   enrollment = db.IntField(min_value=0)
   hours = db.ListField(db.ReferenceField(Hour))

class Lecture(db.Document): # subclasses Course, has specific instructor & classroom number?
   number = db.StringField(max_length=255, required=True, unique=True) #eg 3
   professor = db.ReferenceField(Instructor)
   location = db.ReferenceField(Room)
   date_of_final = db.DateTimeField()
   hours = db.ListField(db.ReferenceField(Hour))
   sections = db.ListField(db.ReferenceField(Section))
   # USER SUBMITTED PHOTOS, MOTHAFUCKA. (URL? GridFS?)
   # http://docs.mongodb.org/manual/core/gridfs/ 

###### Dining ###### 

class Food(db.Document):
    name = db.StringField(max_length=255, required=True, unique=True)
    ingredients = db.ListField(db.StringField(max_length=255))

class Menu(db.Document):
    date = db.DateTimeField(required=True) 
    foods = db.ListField(db.ReferenceField(Food))

class Restaurant(db.Document):
    name = db.StringField(max_length=255, required=True, unique=True)
    menus = db.ListField(db.ReferenceField(Menu))
    hours = db.ListField(db.ReferenceField(Hour))

##### Buildings #####

class Building(db.Document):
    name = db.StringField(max_length=255, required=True, unique=True)
    rooms = db.ListField(db.ReferenceField(Room))
    amenities = db.ListField(db.StringField())
    #geolocationfield! Flask says it doesn't support this field. 
    # does that mean there's no way we can use it?

class Library(db.Document):
    name = db.StringField(max_length=255, required=True, unique=True)
    hours = db.ListField(db.ReferenceField(Hour))

