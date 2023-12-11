#!/usr/bin/python3
"""start of methode"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """def states_list"""
    from models.state import State
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())

    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown():
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)