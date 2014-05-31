import os
from mongoengine import connect

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods

from flask import render_template

app = Flask(__name__)
app.debug = True

app.config["MONGODB_DB"] = 'app25845098'
connect(
        'app25845098',
        username='heroku',
        password='a614e68b445d0d9d1c375740781073b4',
        host='mongodb://lowell:bander@kahana.mongohq.com:10090/app25845098',
        port=10090
)

db = MongoEngine(app)
api = MongoRest(app)

@app.route('/')
def index():
    return render_template('index.html')

class Course(db.Document):
    title = db.StringField()
    number = db.StringField()
    department = db.StringField()
    description = db.StringField()
    units = db.IntField()

class CourseResource(Resource):
    document = Course
    filters = {
        'number': [ops.Exact, ops.Contains],
        'department': [ops.Exact, ops.Contains],
    }

@api.register(name='course', url='/course/')
class CourseView(ResourceView):
    resource = CourseResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List, methods.Delete]


if __name__ == '__main__':
    app.run()

