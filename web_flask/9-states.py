#!/usr/bin/python3
"""Initiates Flask web app.
Listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page having all State objects.
    /states/<id>: HTML page displaying a given state with <id>.
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Renders HTML page having all States.
    Sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Renders HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Removing current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
