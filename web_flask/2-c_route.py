#!/usr/bin/python3
"""
Scrip with paths: /, /hbnb, /c/<text>
each printing a message and text taking in from path
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display 'Hello HBNB!'"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def cpath():
    """DIsplay 'C' followed by some text"""
    formatted_text = text.replace('_', ' ')
    return (f"C {formatted_text}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
