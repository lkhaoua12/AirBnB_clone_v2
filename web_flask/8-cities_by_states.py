#!/usr/bin/python3
""" render templates with states and cities """
from flask import Flask, render_template
from models import storage, state

app = Flask(__name__)


@app.teardown_appcontext
def close_app(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(state.State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
