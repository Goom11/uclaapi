from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods

app = Flask(__name__)
app.debug = True

app.config.update(
    MONGODB_HOST = 'localhost',
    MONGODB_PORT = '27017',
    MONGO_DB = 'kinetic',
)
