#!/usr/bin/python3
""" rendering pages with varible name """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ render the home page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def homeHbnb():
    """ render the /hbnb page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def homeC(text):
    """ render the /c/<text> page """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def homePython(text="is_cool"):
    """ render the /python/<text> page """
    text = 'is cool' if not text else text
    return f'Python {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
