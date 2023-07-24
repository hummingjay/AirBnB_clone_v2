
# 0x04. AirBnB clone - Web framework

## General

  - What is a Web Framework
  - How to build a web framework with Flask
  - How to define routes in Flask
  - What is a route
  - How to handle variables in a route
  - What is a template
  - How to create a HTML response in Flask by using a template
  - How to create a dynamic template (loops, conditions…)
  - How to display in HTML data from a MySQL database

## Installing flask
```
$ pip3 install Flask
```
## Tasks

0. Hello Flask!
   Write a script that starts a Flask web application:
  - Your web application must be listening on `0.0.0.0`, port `5000`
  - Routes:
    - `/`: display “Hello HBNB!”
  - You must use the option `strict_slashes=False` in your route definition </br>

File: [0-hello\_route.py](0-hello_route.py), [\_\_init\_\_.py](__init__.py)

1. HBNB
   Write a script that starts a Flask web application:

   - Your web application must be listening on 0.0.0.0, port 5000
   - Routes:
    - `/`: display “Hello HBNB!”
    - `/hbnb`: display “HBNB”
   - You must use the option `strict_slashes=False` in your route definition </br>

File: [1-hbnb\_route.py](1-hbnb_route.py)

2. C is fun!
Write a script that starts a Flask web application:

  - Your web application must be listening on 0.0.0.0, port 5000
  - Routes:
    - `/`: display “Hello HBNB!”
    - `/hbnb`: display “HBNB”
    - `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space )
  - You must use the option `strict_slashes=False` in your route definition </br>

File: [2-c\_route.py](2-c_route.py)
