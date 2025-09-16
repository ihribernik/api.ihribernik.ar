"""
Domain-specific exceptions for the blog application.
Provides a comprehensive hierarchy of exceptions for domain-specific errors.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class BlogException(Exception):
    """Base exception for all domain exceptions."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.timestamp = datetime.now(timezone.utc)
        self.details = details
        super().__init__(message)


class DomainValidationError(BlogException):
    """Base class for all domain validation errors."""

    def __init__(self, message: str, validation_errors: List[str]):
        details = {"validation_errors": validation_errors}
        super().__init__(message, details)
        self.validation_errors = validation_errors


class PostNotFoundError(BlogException):
    """Raised when a requested post is not found."""

    def __init__(self, post_id: str):
        message = f"Post with id {post_id} not found"
        super().__init__(message, {"post_id": post_id})


class InvalidPostError(DomainValidationError):
    """Raised when post validation fails."""

    def __init__(self, errors: List[str]):
        super().__init__("Post validation failed", errors)


class UnauthorizedError(BlogException):
    """Raised when user is not authorized to perform an action."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(BlogException):
    """Raised when domain validation fails."""

    pass


class PostError(BlogException):
    """Base class for post-related errors."""

    pass


class PostNotFound(PostError):
    """Raised when a post is not found."""

    def __init__(self, post_id: int):
        super().__init__(f"Post with ID {post_id} not found")
        self.post_id = post_id


class PostAlreadyExists(PostError):
    """Raised when trying to create a post with a duplicate title."""

    def __init__(self, title: str):
        super().__init__(f"Post with title '{title}' already exists")
        self.title = title


class PostValidationError(PostError, ValidationError):
    """Raised when post validation fails."""

    pass


class RepositoryError(BlogException):
    """Base class for repository-related errors."""

    pass


class DatabaseError(RepositoryError):
    """Raised when a database operation fails."""

    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.original_error = original_error


class ConnectionError(DatabaseError):
    """Raised when database connection fails."""

    pass


class TransactionError(DatabaseError):
    """Raised when database transaction fails."""

    pass


class AuthorizationError(BlogException):
    """Raised when authorization fails."""

    pass


class RateLimitError(BlogException):
    """Raised when rate limit is exceeded."""

    def __init__(self, limit: int, window: int):
        super().__init__(
            f"Rate limit of {limit} requests per {window} seconds exceeded"
        )
        self.limit = limit
        self.window = window
