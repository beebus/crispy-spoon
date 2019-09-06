from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template('food.html', food=food)
