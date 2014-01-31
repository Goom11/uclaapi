from uclaapi import db

class Class(db.Document):
   name = db.StringField(max_length=255, required=True)

class Textbook(db.Document):
   name = db.StringField(max_length=255, required=True)
