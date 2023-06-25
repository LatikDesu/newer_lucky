from flask import Blueprint, render_template, request
from main_compiler import main

bp = Blueprint('editor', __name__)


@bp.route('/editor', methods=["GET", "POST"])
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
