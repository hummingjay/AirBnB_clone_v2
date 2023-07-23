#!/usr/bin/python3
"""
script that starts a Flask web application:
    with paths: /, /hbnb
"""

from flask import FLASK
app = Flask(__name)


@app.route('/', strict_slashes=False)
def index():
    """Return Hello world!"""
    return ('Hello HBNB')


@app.route('/hbnb', strict_slashes=False)
def index():
    """Return HBNB"""
    return ("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
