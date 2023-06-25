from loguru import logger

from flask import Flask
from flask_cors import CORS
from api import api
from views import bp

logger_format = ('{time:HH:mm:ss}'
                 ' | '
                 '({elapsed.seconds}s)'
                 ' --> '
                 '{message}')

logger.add("static/job.log", format=logger_format, encoding="utf-8")

app = Flask(__name__, static_folder="static", template_folder='templates')

api.init_app(app)
app.register_blueprint(bp, url_prefix='/editor')

CORS(app)

if __name__ == "__main__":
    app.run(port=5000, host="localhost")
