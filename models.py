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

# TODO: model(s) for dining hours
# TODO: model(s) for dining menus
# TODO: specify pks / which fields are unique.
    # how are we going to index at the endpoints?
