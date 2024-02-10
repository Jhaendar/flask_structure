from flask import redirect, render_template, request, url_for

from flask_structure.app.extensions import db
from flask_structure.app.models.question import Question
from flask_structure.app.questions import bp


@bp.route("/", methods=(["GET"]))
def index():
    questions = Question.query.all()

    return render_template("questions/index.html", questions=questions)


@bp.route("/", methods=(["POST"]))
def submit():
    new_question = Question(
        content=request.form["content"], answer=request.form["answer"]
    )

    db.session.add(new_question)
    db.session.commit()
    return redirect(url_for("questions.index"))
