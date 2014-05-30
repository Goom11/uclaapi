import os

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
    MONGODB_DB = 'chimera',
)

db = MongoEngine(app)
api = MongoRest(app)

class Course(db.Document):
    title = db.StringField()
    number = db.StringField()
    department = db.StringField()
    description = db.StringField()

class CourseResource(Resource):
    document = Course
    filters = {
        'number': [ops.Exact]
    }

@api.register(name='course', url='/course/')
class CourseView(ResourceView):
    resource = CourseResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List, methods.Delete]


if __name__ == '__main__':
    app.run()

