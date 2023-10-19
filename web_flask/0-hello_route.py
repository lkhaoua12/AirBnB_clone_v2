#!/usr/bin/python3
""" start a Flask app that renders Hello, World!"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_flask():
    """ render hello hbnb whene called """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
