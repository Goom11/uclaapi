import os
from flask import Flask


app = Flask(__name__)
db = MongoEngine(app)

@app.route('/')
def home():
    return 'hello werld'

