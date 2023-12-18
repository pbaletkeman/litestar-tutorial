from __future__ import annotations

from uuid import UUID

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from step1.model.author import AuthorModel


class BookModel(UUIDAuditBase):
    __tablename__ = "book"  # type: ignore[assignment]
    title: Mapped[str]
    author_id: Mapped[UUID] = mapped_column(ForeignKey("author.id"))
    author: Mapped["AuthorModel"] = relationship(lazy="joined", innerjoin=True, viewonly=True)
