# Basic flask application

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    print(request.method)
    print(request.headers)
    return '<h1>Learning Flask</h1>'


@app.route('/user/<name>')
def user(name):
    return 'Hello, %s' % format(name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404