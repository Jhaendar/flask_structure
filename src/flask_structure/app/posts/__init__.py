from flask import Blueprint

bp = Blueprint("posts", __name__)


from flask_structure.app.posts import routes  # noqa: E402, F401
