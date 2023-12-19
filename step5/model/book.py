from __future__ import annotations

from uuid import UUID

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from step5.common import BaseModel


class BookModel(UUIDAuditBase):
    __tablename__ = "book"
    title: Mapped[str]
    author_id: Mapped[UUID] = mapped_column(ForeignKey("author.id"))
    author: Mapped["AuthorModel"] = relationship(lazy="joined")


class Book(BaseModel):
    id: UUID | None
    title: str
    author_id: UUID


class BookCreate(BaseModel):
    title: str
    author_id: UUID


class BookUpdate(BaseModel):
    title: str | None = None
    author_id: UUID
