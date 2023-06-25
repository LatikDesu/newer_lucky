from flask import Blueprint, render_template, request, Response
from main_compiler import main

bp = Blueprint('editor', __name__)


@bp.route('/', methods=["GET", "POST"])
def index():
    errors = ""
    if request.method == "POST":
        link = None
        try:
            link = request.form["link"]
            model = request.form["model"]
            if model == "":
                model = "base"
        except:
            errors += "<p>{!r} is not a valid link.</p>\n".format(request.form["link"])
        if link is not None:
            result = main(link, model)
            return render_template("home.html", result=result)
    return render_template("home.html", errors=errors)


def flask_logger():
    with open("static/job.log", encoding="utf-8") as log_info:
        data = log_info.read()
        yield data.encode()
    open("static/job.log", 'w').close()


@bp.route('/logs', methods=["GET"])
def stream():
    return Response(flask_logger(), mimetype="text/plain", content_type="text/event-stream")
