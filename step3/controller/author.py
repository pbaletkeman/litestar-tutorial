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
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from step3.model.author import AuthorModel, Author, AuthorCreate, AuthorUpdate

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AuthorRepository(SQLAlchemyAsyncRepository[AuthorModel]):
    """Author repository."""

    model_type = AuthorModel


async def provide_authors_repo(db_session: AsyncSession) -> AuthorRepository:
    """This provides the default Authors repository."""
    return AuthorRepository(session=db_session)


async def provide_author_details_repo(db_session: AsyncSession) -> AuthorRepository:
    """This provides a simple example demonstrating how to override the join options for the repository."""
    return AuthorRepository(
        statement=select(AuthorModel).options(selectinload(AuthorModel.books)),
        session=db_session,
    )


class AuthorController(Controller):
    """Author CRUD"""

    dependencies = {"authors_repo": Provide(provide_authors_repo)}
    path = "/authors"
    tags = ["Author CRUD"]

    @get()
    async def list_authors(
            self,
            authors_repo: AuthorRepository,
            limit_offset: LimitOffset,
    ) -> OffsetPagination[Author]:
        """List authors."""
        results, total = await authors_repo.list_and_count(limit_offset)
        type_adapter = TypeAdapter(list[Author])
        return OffsetPagination[Author](
            items=type_adapter.validate_python(results),
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @post()
    async def create_author(
            self,
            authors_repo: AuthorRepository,
            data: AuthorCreate,
    ) -> Author:
        """Create a new author."""
        obj = await authors_repo.add(
            AuthorModel(**data.model_dump(exclude_unset=True, exclude_none=True)),
        )
        await authors_repo.session.commit()
        return Author.model_validate(obj)

    @get(path="/{author_id:uuid}")
    async def get_author(
            self,
            authors_repo: AuthorRepository,
            author_id: UUID = Parameter(
                title="Author ID",
                description="The author to retrieve.",
            ),
    ) -> Author:
        """Get an existing author."""
        obj = await authors_repo.get(author_id)
        return Author.model_validate(obj)

    @put(path="/{author_id:uuid}")
    async def put_author(
            self,
            authors_repo: AuthorRepository,
            data: AuthorUpdate,
            author_id: UUID = Parameter(
                title="Author ID",
                description="The author to update.",
            ),
    ) -> Author:
        """Update an author, including empty values."""
        raw_obj = data.model_dump(exclude_unset=False, exclude_none=False)
        raw_obj.update({"id": author_id})
        obj = await authors_repo.update(AuthorModel(**raw_obj))
        await authors_repo.session.commit()
        return Author.model_validate(obj)

    @patch(path="/{author_id:uuid}")
    async def patch_author(
            self,
            authors_repo: AuthorRepository,
            data: AuthorUpdate,
            author_id: UUID = Parameter(
                title="Author ID",
                description="The author to update.",
            ),
    ) -> Author:
        """Update an author, ignoring empty values."""
        raw_obj = data.model_dump(exclude_unset=True, exclude_none=True)
        raw_obj.update({"id": author_id})
        obj = await authors_repo.update(AuthorModel(**raw_obj))
        await authors_repo.session.commit()
        return Author.model_validate(obj)

    @delete(path="/{author_id:uuid}")
    async def delete_author(
            self,
            authors_repo: AuthorRepository,
            author_id: UUID = Parameter(
                title="Author ID",
                description="The author to delete.",
            ),
    ) -> None:
        """Delete a author from the system."""
        _ = await authors_repo.delete(author_id)
        await authors_repo.session.commit()
