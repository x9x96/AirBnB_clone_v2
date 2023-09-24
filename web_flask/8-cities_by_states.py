#!/usr/bin/python3
"""Initiates Flask web app.
Listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page having all states and related cities.
"""
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """An HTML page having all State and related cities.
    Sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removing current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
