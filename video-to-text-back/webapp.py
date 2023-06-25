from flask import Flask, render_template, request
from flask_cors import CORS
from api import api
from views import bp

app = Flask(__name__, template_folder='templates')

api.init_app(app)
app.register_blueprint(bp)

CORS(app)

if __name__ == "__main__":
    app.run(port=5000, host="localhost")
