"""FastAPI error handling middleware."""

import logging
from typing import Any, Dict, Optional

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.domain.exceptions import (
    BlogException,
    ConnectionError,
    DatabaseError,
    DomainValidationError,
    InvalidPostError,
    PostNotFoundError,
    TransactionError,
    UnauthorizedError,
)

logger = logging.getLogger(__name__)


def create_error_response(
    status_code: int,
    error_type: str,
    message: str,
    details: Optional[Dict[str, Any]] = None,
) -> JSONResponse:
    """Create a standardized error response."""
    content = {
        "error": error_type,
        "message": message,
    }
    if details:
        content["details"] = details

    return JSONResponse(
        status_code=status_code,
        content=content,
    )


def add_error_handlers(app: FastAPI) -> None:
    """Add exception handlers to the FastAPI application."""

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        """Handle FastAPI request validation errors."""
        return create_error_response(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_type="Validation Error",
            message="Invalid request parameters",
            details={"errors": exc.errors()},
        )

    @app.exception_handler(DomainValidationError)
    async def domain_validation_handler(
        request: Request, exc: DomainValidationError
    ) -> JSONResponse:
        """Handle domain validation errors."""
        return create_error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error_type="VALIDATION_ERROR",
            message=str(exc),
            details={"errors": exc.validation_errors},
        )

    @app.exception_handler(PostNotFoundError)
    async def post_not_found_handler(
        request: Request, exc: PostNotFoundError
    ) -> JSONResponse:
        """Handle post not found errors."""
        return create_error_response(
            status_code=status.HTTP_404_NOT_FOUND,
            error_type="NOT_FOUND",
            message=str(exc),
            details=exc.details,
        )

    @app.exception_handler(InvalidPostError)
    async def invalid_post_handler(
        request: Request, exc: InvalidPostError
    ) -> JSONResponse:
        """Handle invalid post errors."""
        return create_error_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            error_type="INVALID_POST",
            message=str(exc),
            details={"errors": exc.validation_errors},
        )

    @app.exception_handler(UnauthorizedError)
    async def auth_error_handler(
        request: Request, exc: UnauthorizedError
    ) -> JSONResponse:
        """Handle authorization errors."""
        return create_error_response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_type="UNAUTHORIZED",
            message=str(exc),
            details=exc.details,
        )

    @app.exception_handler(ConnectionError)
    async def connection_error_handler(
        request: Request, exc: ConnectionError
    ) -> JSONResponse:
        """Handle database connection errors."""
        logger.error(f"Database connection error: {exc}")
        return create_error_response(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            error_type="CONNECTION_ERROR",
            message="Database connection failed",
            details=exc.details,
        )

    @app.exception_handler(TransactionError)
    async def transaction_error_handler(
        request: Request, exc: TransactionError
    ) -> JSONResponse:
        """Handle database transaction errors."""
        logger.error(f"Database transaction error: {exc}")
        return create_error_response(
            status_code=status.HTTP_409_CONFLICT,
            error_type="TRANSACTION_ERROR",
            message="Database transaction failed",
            details=exc.details,
        )

    @app.exception_handler(DatabaseError)
    async def database_error_handler(
        request: Request, exc: DatabaseError
    ) -> JSONResponse:
        """Handle general database errors."""
        logger.error(f"Database error: {exc}")
        return create_error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type="DATABASE_ERROR",
            message="Database operation failed",
            details=exc.details,
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error_handler(
        request: Request, exc: SQLAlchemyError
    ) -> JSONResponse:
        """Handle unexpected SQLAlchemy errors."""
        logger.error(f"Unexpected SQLAlchemy error: {exc}", exc_info=exc)
        return create_error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type="DATABASE_ERROR",
            message="An unexpected database error occurred",
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request, exc: StarletteHTTPException
    ) -> JSONResponse:
        """Handle HTTP exceptions."""
        return create_error_response(
            status_code=exc.status_code,
            error_type="HTTP_ERROR",
            message=str(exc.detail),
        )

    @app.exception_handler(BlogException)
    async def blog_exception_handler(
        request: Request, exc: BlogException
    ) -> JSONResponse:
        """Handle generic blog exceptions."""
        logger.error(f"Blog exception: {exc}")
        return create_error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type="APPLICATION_ERROR",
            message=str(exc),
            details=exc.details,
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request, exc: Exception
    ) -> JSONResponse:
        """Handle any unhandled exceptions."""
        logger.error(f"Unhandled error: {exc}", exc_info=exc)
        return create_error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_type="INTERNAL_SERVER_ERROR",
            message="An unexpected error occurred",
        )
