#!/usr/bin/python3
""" list states page and cities page """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def route_states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all(State).values()
    found_state = None
    for state in states:
        if state.id == id:
            found_state = state
    return render_template("9-states.html", state=found_state)


@app.teardown_appcontext
def app_teardown(exception):
    """ close db each request is made """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
