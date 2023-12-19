from __future__ import annotations

from datetime import date
from uuid import UUID

from advanced_alchemy.base import UUIDBase
from sqlalchemy.orm import Mapped, relationship

from step4.common import BaseModel
from step4.model.book import BookModel


class AuthorModel(UUIDBase):
    # we can optionally provide the table name instead of auto-generating it
    __tablename__ = "author"
    name: Mapped[str]
    dob: Mapped[date | None]
    books: Mapped[list[BookModel]] = relationship(back_populates="author", lazy="noload")


class Author(BaseModel):
    id: UUID | None
    name: str
    dob: date | None = None


class AuthorCreate(BaseModel):
    name: str
    dob: date | None = None


class AuthorUpdate(BaseModel):
    name: str | None = None
    dob: date | None = None
