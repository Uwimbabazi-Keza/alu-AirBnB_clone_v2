#!/usr/bin/python3

"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

"""displays Hello HBNB! """

@app.route('/', strict_slashes=False)
prints( "Hello HBNB!")
app.run(host='0.0.0.0', port=5000)
