import os
import json
import datetime
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'uclaapi_test'}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

from models import *

def getDict(inputObj, fields):
    obj = inputObj.__dict__['_data']
    fields = [(field, obj[field]) for field in fields if field in obj]
    result = {key: value for (key, value) in fields}
    return result


@app.route('/temp')
def myfunc():
    fields = ['title', 'units', 'description', 'number']
    result = [getDict(temp, fields) for temp in Temp.objects]
    return json.dumps(result)


@app.route('/')
def home():
    temps = Temp.objects
    string = ""
    for temp in temps:
        string += temp.title + '\n'
    return string
    return 'hello werld'


@app.route('/api/v1/classes')
def get_class_list():
    return 'classes'


@app.route('/api/v1/classes/<int:class_id>')
def get_class_info(class_id):
    return 'class info'


@app.route('/api/v1/textbooks')
def get_book_list():
    return 'books'


@app.route('/api/v1/textbooks/<int:book_id>')
def get_book_info(book_id):
    return 'book info'
