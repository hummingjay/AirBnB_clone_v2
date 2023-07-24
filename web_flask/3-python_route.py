#!/usr/bin/python3
"""
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, then value of the text
/python/(<text>): display “Python ”, then value of text
The default value of text is “is cool”
"""
from flask import Flask
app = FLASK(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cpath(text):
    """ returns 'C' followed by text in route """
    formatted_text = text.replace('_', ' ')
    return (f"C {formatted_text}")


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def pypath(text='is cool'):
    """returns python followed by text in url"""
    formatted_text = text.replace('_', ' ')
    return (f"Python {formatted_text}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
