from flask import render_template

from flask_structure.app.main import bp


@bp.route("/")
def index():
    return render_template("index.html")
