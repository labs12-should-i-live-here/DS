from flask import Flask, request
from decouple import config
from flask_json import FlaskJSON, JsonError, json_response
import requests

# Create and configure an instance of the Flask application.
application = app = Flask(__name__)
FlaskJSON(app)

@app.route('/')
def root():
    """
    Testing elastic bean
    """
    return "Test Successful"

if __name__ == '__main__':
    application.run(debug=True)
