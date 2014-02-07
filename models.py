from uclaapi import db

# Textbooks/Registrar

class Textbook(db.Document):
   title = db.StringField(max_length=255, required=True)
   SKU = db.StringField(max_length=255, required=True)
   new_price = db.DecimalField(min_value=0)
   used_price = db.DecimalField(min_value=0)

class Course(db.Document):
   name = db.StringField(max_length=255, required=True, unique=True)
   instructor = db.StringField(max_length=255, required=True, unique=True)
   books = db.ListField(db.ReferenceField(Textbook))

# Dining

class Restaurant(db.Document)
   name = db.StringField(max_length=255, required=True, unique=True)
   breakfast = db.ListField(db.ReferenceField(Hours))
   lunch = db.ListField(db.ReferenceField(Hours))
   dinner = db.ListField(db.ReferenceField(Hours))
   #menu(s?)

class Menu(db.Document):
   date = db.DateTimeField(required=True) 
   foods = db.ListField(db.ReferenceField(Food))

class Food(db.Document):
   name = db.StringField(max_length=255, required=True, unique=True)

class Hours(db.Document):
   open = db.DecimalField(min_value=0)
   close = db.DecimalField(min_value=0)
   # -1 means closed?

# TODO: model(s) for dining hours
# TODO: model(s) for dining menus
# TODO: specify pks / which fields are unique.
    # how are we going to index at the endpoints?
