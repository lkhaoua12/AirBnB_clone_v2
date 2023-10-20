#!/usr/bin/python3
""" rendering pages with varible name """

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def homePython(text="is_cool"):
    """ render the /python/<text> page """
    return f"python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def homeNumber(n):
    """ render the /number/<n> page """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def homeTemplate(n):
    """ render templates with passed argument """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def homeTemplateIf(n):
    """ render templates with passed argument """
    is_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, is_even=is_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
