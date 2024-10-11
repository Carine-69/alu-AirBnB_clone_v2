#!/usr/bin/python3
"""Starts a Flask web application for HBNB project"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

# Handle teardown to close the storage after each request
@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display the HBNB page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    # Sort the data by name (A->Z)
    states = sorted(states, key=lambda s: s.name)
    amenities = sorted(amenities, key=lambda a: a.name)
    places = sorted(places, key=lambda p: p.name)

    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

