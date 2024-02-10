from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from flask_structure.app.extensions import db


class Post(db.Model):  # type: ignore
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    content: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f'<Post "{self.title}">'
