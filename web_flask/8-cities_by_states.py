#!/usr/bin/python3
""" Create server with default main page """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """def index"""
    return "Hello HBNB!"


@app.teardown_appcontext
def afterRequest(self):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """def cities_by_states"""
    from models.state import State
    from models.city import City

    states = storage.all(State).values()
    cities = storage.all(City).values()

    return render_template('8-cities_by_states.html',
                           cities=cities,
                           states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
