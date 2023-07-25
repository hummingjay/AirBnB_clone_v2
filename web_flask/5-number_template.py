#!/usr/bin/python3
"""
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, then value of the text
/python/(<text>): display “Python ”, then value of text
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is int
"""
from flask import Flask, render_template
app = Flask(__name__)


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
@app.route('/python/<text>', strict_slashes=False)
def pypath(text='is cool'):
    """returns python followed by text in url"""
    formatted_text = text.replace('_', ' ')
    return (f"Python {formatted_text}")


# use int to tell flask expect int and pass if int
@app.route('/number/<int:n>', strict_slashes=False)
def npath(n):
    """Print n is a number if n is int"""
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def templath(n):
    """ render page if n is integer"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
