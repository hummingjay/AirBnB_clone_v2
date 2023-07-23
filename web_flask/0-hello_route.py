#!/usr/bin/python3
"""
Flask Web application displays "Hello HBNB!"
"""

from flask import Flask

# create flask instance
app = Flask(__name__)

# create a router with a decorator
# / first page


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB!"""
    return ("Hello HBNB!")


if __name__ == '__main__':
    # Specify ip to run on and port to listen to
    app.run(host='0.0.0.0', port=5000)
