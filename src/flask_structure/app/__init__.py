from flask import Flask

from flask_structure.app.extensions import db
from flask_structure.config import FlaskConfig


def create_app(config_class=FlaskConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from flask_structure.app.main import bp as main_bp

    app.register_blueprint(main_bp)

    from flask_structure.app.posts import bp as posts_bp

    app.register_blueprint(posts_bp, url_prefix="/posts")

    from flask_structure.app.questions import bp as questions_bp

    app.register_blueprint(questions_bp, url_prefix="/questions")

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
