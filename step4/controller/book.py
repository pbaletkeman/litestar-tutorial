from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository
from pydantic import TypeAdapter

from litestar import get
from litestar.controller import Controller
from litestar.di import Provide
from litestar.handlers.http_handlers.decorators import delete, patch, post, put
from litestar.pagination import OffsetPagination
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset

from step4.model.book import BookModel, Book, BookCreate, BookUpdate

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class BookRepository(SQLAlchemyAsyncRepository[BookModel]):
    """Author repository."""

    model_type = BookModel


async def provide_book_repo(db_session: AsyncSession) -> BookRepository:
    """This provides the default Authors repository."""
    return BookRepository(session=db_session)


class BookController(Controller):
    """Book CRUD"""

    dependencies = {"book_repo": Provide(provide_book_repo)}
    path = "/book"
    tags = ["Book CRUD"]

    @get()
    async def list_books(
        self,
        book_repo: BookRepository,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[Book]:
        """List books."""
        results, total = await book_repo.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[Book])
        return OffsetPagination[Book](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @post()
    async def create_book(
        self,
        book_repo: BookRepository,
        data: BookCreate,
    ) -> Book:
        """Create a new book."""
        obj = await book_repo.add(
            BookModel(**data.model_dump(exclude_unset=True, exclude_none=True)),
        )
        await book_repo.session.commit()
        return Book.model_validate(obj)

    @get(path="/{book_id:uuid}")
    async def get_book(
        self,
        book_repo: BookRepository,
        book_id: UUID = Parameter(
            title="Book ID",
            description="The book to retrieve.",
        ),
    ) -> Book:
        """Get an existing book."""
        obj = await book_repo.get(book_id)
        return Book.model_validate(obj)

    @put(path="/{book_id:uuid}",)
    async def put_book(
            self,
            book_repo: BookRepository,
            data: BookUpdate,
            book_id: UUID = Parameter(
                title="Book ID",
                description="The book to update.",
            ),
    ) -> Book:
        """Update a book, including empty values."""
        raw_obj = data.model_dump(exclude_unset=False, exclude_none=False)
        raw_obj.update({"id": book_id})
        obj = await book_repo.update(BookModel(**raw_obj))
        await book_repo.session.commit()
        return Book.model_validate(obj)

    @patch(path="/{book_id:uuid}",)
    async def patch_book(
        self,
        book_repo: BookRepository,
        data: BookUpdate,
        book_id: UUID = Parameter(
            title="Book ID",
            description="The book to update.",
        ),
    ) -> Book:
        """Update a book, ignoring empty values."""
        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": book_id})
        obj = await book_repo.update(BookModel(**raw_obj))
        await book_repo.session.commit()
        return Book.model_validate(obj)

    @delete(path="/{book_id:uuid}")
    async def delete_book(
        self,
        book_repo: BookRepository,
        book_id: UUID = Parameter(
            title="Book ID",
            description="The book to delete.",
        ),
    ) -> None:
        """Delete a book from the system."""
        _ = await book_repo.delete(book_id)
        await book_repo.session.commit()
