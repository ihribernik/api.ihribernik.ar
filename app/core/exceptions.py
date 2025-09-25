"""
Domain-specific exceptions for the blog application.
Provides a comprehensive hierarchy of exceptions for domain-specific errors.
"""
from __future__ import annotations

from datetime import datetime
from datetime import timezone
from typing import Any


class PostException(Exception):
    """Base exception for all domain exceptions."""

    def __init__(self, message: str, details: dict[str, Any] | None = None):
        self.timestamp = datetime.now(timezone.utc)
        self.details = details
        super().__init__(message)


class DomainValidationError(PostException):
    """Base class for all domain validation errors."""

    def __init__(self, message: str, validation_errors: list[str]):
        details = {'validation_errors': validation_errors}
        super().__init__(message, details)
        self.validation_errors = validation_errors


class PostNotFoundError(PostException):
    """Raised when a requested post is not found."""

    def __init__(self, post_id: str):
        message = f"Post with id {post_id} not found"
        super().__init__(message, {'post_id': post_id})


class InvalidPostError(DomainValidationError):
    """Raised when post validation fails."""

    def __init__(self, errors: list[str]):
        super().__init__('Post validation failed', errors)


class UnauthorizedError(PostException):
    """Raised when user is not authorized to perform an action."""

    def __init__(self, message: str, details: dict[str, Any] | None = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(PostException):
    """Raised when domain validation fails."""

    pass


class PostError(PostException):
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


class RepositoryError(PostException):
    """Base class for repository-related errors."""

    pass


class DatabaseError(RepositoryError):
    """Raised when a database operation fails."""

    def __init__(self, message: str, original_error: Exception | None = None):
        super().__init__(message)
        self.original_error = original_error


class ConnectionError(DatabaseError):
    """Raised when database connection fails."""

    pass


class TransactionError(DatabaseError):
    """Raised when database transaction fails."""

    pass


class AuthorizationError(PostException):
    """Raised when authorization fails."""

    pass


class RateLimitError(PostException):
    """Raised when rate limit is exceeded."""

    def __init__(self, limit: int, window: int):
        super().__init__(
            f"Rate limit of {limit} requests per {window} seconds exceeded",
        )
        self.limit = limit
        self.window = window
