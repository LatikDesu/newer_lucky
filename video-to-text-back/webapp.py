from flask import Flask, render_template, request
from flask_cors import CORS
from api import api

app = Flask(__name__)
CORS(app)

api.init_app(app)

if __name__ == "__main__":
    app.run(port=5000, host="localhost")
