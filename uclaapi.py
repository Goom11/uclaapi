import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'uclaapi_test'}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


@app.route('/')
def home():
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
