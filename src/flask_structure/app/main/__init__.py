from flask import Blueprint

bp = Blueprint("main", __name__)

from flask_structure.app.main import routes  # noqa: E402, F401
