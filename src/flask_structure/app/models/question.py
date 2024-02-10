from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from flask_structure.app.extensions import db


class Question(db.Model):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f"<Question {self.content}>"
