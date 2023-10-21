#!/usr/bin/python3
""" renders the filter section """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def app_teardown(exception):
    """ close db each request is made """
    storage.close()


@app.route('/hbnb_filters')
def handle_filters():
    """ handle filters rendring """
    states = storage.all(State).values()
    return render_template('10-hbnb_filters.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
