from flask import Blueprint

bp = Blueprint("questions", __name__)

from flask_structure.app.questions import routes  # noqa: E402, F401
