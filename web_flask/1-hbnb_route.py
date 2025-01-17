#!/usr/bin/python3
""" this modules start a flask server that route / and /hbnb """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ render the home page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def helloHbnb():
    """ render the /hbnb page """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
