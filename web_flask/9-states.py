#!/usr/bin/python3
"""Web App with Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def slash_state():
    state = storage.all(State).values()

    return render_template('9-states.html',
                           states=state,
                           road="state_road")


@app.route('/states/<id>', strict_slashes=False)
def cities_in_state(id):
    """Display a HTML page with a list of all State objects in DBStorage."""
    states = storage.all(State).values()

    for state in states:
        if state.id == id:
            city = state.cities
            return render_template('9-states.html',
                                   states=states,
                                   cities=city,
                                   state=state,
                                   road="city_road")

    return render_template('9-states.html', road="not found")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
