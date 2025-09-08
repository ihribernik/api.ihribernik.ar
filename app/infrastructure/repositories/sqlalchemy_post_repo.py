from typing import List, Optional

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.domain.exceptions import (
    BlogException,
    DomainValidationError,
)
from app.domain.models.post import Post as DomainPost
from app.domain.ports.post_repository import PostRepository
from app.infrastructure.database.models import Post


class DatabaseError(BlogException):
    """Base exception for database-related errors."""

    def __init__(self, message: str, original_error: Optional[Exception] = None):
        details = {"original_error": str(original_error)} if original_error else None
        super().__init__(message, details)


class ConnectionError(DatabaseError):
    """Raised when database connection fails."""

    pass


class TransactionError(DatabaseError):
    """Raised when a database transaction fails."""

    pass


class RepositoryError(DatabaseError):
    """Raised when a repository operation fails."""

    pass


class SqlAlchemyPostRepository(PostRepository):
    """
    SQLAlchemy implementation of the PostRepository port.
    Handles persistence of Post entities using a SQLAlchemy session.
    """

    @staticmethod
    def _to_domain_post(db_post: Post) -> DomainPost:
        """Convert database Post model to domain Post model."""
        return DomainPost(
            id=db_post.id,
            title=db_post.title,
            content=db_post.content,
            author=db_post.author,
            created_at=db_post.created_at,
            updated_at=db_post.updated_at,
        )

    @staticmethod
    def _from_domain_post(domain_post: DomainPost) -> Post:
        """Convert domain Post model to database Post model."""
        return Post(
            id=domain_post.id if hasattr(domain_post, "id") else None,
            title=domain_post.title,
            content=domain_post.content,
            author=domain_post.author,
            created_at=domain_post.created_at,
            updated_at=domain_post.updated_at,
        )

    def __init__(self, session: Session) -> None:
        """
        Initialize repository with a SQLAlchemy session.

        Args:
            session (Session): SQLAlchemy session instance
        """
        self.session = session
        self.check_connection()

    def check_connection(self) -> None:
        """
        Check if database connection is available.
        Raises:
            ConnectionError: If connection fails
            DatabaseError: For any other database error
        """
        try:
            self.session.execute(text("SELECT 1"))
            self.session.commit()
        except OperationalError as e:
            raise ConnectionError("Database connection failed", original_error=e)
        except SQLAlchemyError as e:
            raise DatabaseError(
                "Failed to configure database session", original_error=e
            )

    def save(self, post: DomainPost) -> DomainPost:
        """
        Save a post to the database.
        If post with same title exists, raise InvalidPostError.
        If database error occurs, raise DatabaseError.

        Args:
            post (DomainPost): The post to save

        Returns:
            DomainPost: The saved post with updated ID

        Raises:
            InvalidPostError: If post validation fails or duplicate title
            DatabaseError: If database error occurs
            TransactionError: If database integrity error occurs
        """
        db_post = self._from_domain_post(post)
        try:
            stmt = (
                insert(Post)
                .values(
                    title=db_post.title,
                    content=db_post.content,
                    author=db_post.author,
                    created_at=db_post.created_at,
                    updated_at=db_post.updated_at,
                )
                .on_conflict_do_nothing()
            )

            result = self.session.execute(stmt)

            if result.rowcount == 0:
                raise DomainValidationError(
                    "Post validation failed",
                    [f"A post with title '{post.title}' already exists"],
                )

            self.session.commit()
            return self._to_domain_post(db_post)

        except IntegrityError as e:
            self.session.rollback()
            raise TransactionError("Database integrity error", original_error=e)
        except SQLAlchemyError as e:
            self.session.rollback()
            raise DatabaseError(f"Error saving post: {str(e)}", original_error=e)

    def get_all(self) -> List[DomainPost]:
        """
        Get all posts.
        If database error occurs, raises DatabaseError.

        Returns:
            List[DomainPost]: List of all posts

        Raises:
            RepositoryError: If error occurs while retrieving posts
        """
        try:
            results = self.session.query(Post).all()
            return [self._to_domain_post(post) for post in results]
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RepositoryError(f"Error retrieving posts: {str(e)}", original_error=e)

    def get_by_id(self, post_id: int) -> DomainPost | None:
        """
        Get a post by its ID.
        If post not found, returns None.
        If database error occurs, raises DatabaseError.

        Args:
            post_id (int): ID of the post to get

        Returns:
            Optional[DomainPost]: The found post or None

        Raises:
            DatabaseError: If database error occurs
        """
        try:
            result = self.session.query(Post).filter(Post.id == post_id).first()
            return self._to_domain_post(result) if result else None
        except SQLAlchemyError as e:
            self.session.rollback()
            raise DatabaseError(f"Error finding post: {str(e)}", original_error=e)
