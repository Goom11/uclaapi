from uclaapi import db


class Class(db.Document):
    course_name = db.StringField(max_length=255, required=True, unique=True)
    instructor = db.StringField(max_length=255, required=True, unique=True)
    books = db.ListField(ReferenceField(Textbook))


class Textbook(db.Document):
    title = db.StringField(max_length=255, required=True)
    SKU = db.StringField(max_length=255, required=True)
    new_price = db.DecimalField(min_value=0)
    used_price = db.DecimalField(min_value=0)
