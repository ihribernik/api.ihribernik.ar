"""FastAPI error handling middleware."""

import logging
from dataclasses import dataclass
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
    status_code: int | None,
    error_type: str,
    message: str,
    details: Optional[Dict[str, Any]] = None,
) -> JSONResponse:
    """Create a standardized error response."""
    content: Dict[str, str | Dict[str, Any]] = {
        "error": error_type,
        "message": message,
    }
    if details:
        content["details"] = details

    return JSONResponse(
        status_code=status_code or status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=content,
    )


@dataclass
class ExceptionHandlerConfig:
    exc_class: type
    status_code: int | None
    error_type: str
    default_message: str | None = None
    log: bool = False


def add_error_handlers(app: FastAPI) -> None:
    """Add exception handlers to the FastAPI application."""

    exception_handlers = [
        ExceptionHandlerConfig(
            RequestValidationError,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "Validation Error",
            "Invalid request parameters",
        ),
        ExceptionHandlerConfig(
            DomainValidationError, status.HTTP_400_BAD_REQUEST, "VALIDATION_ERROR"
        ),
        ExceptionHandlerConfig(
            InvalidPostError, status.HTTP_400_BAD_REQUEST, "INVALID_POST"
        ),
        ExceptionHandlerConfig(
            PostNotFoundError, status.HTTP_404_NOT_FOUND, "NOT_FOUND"
        ),
        ExceptionHandlerConfig(
            UnauthorizedError, status.HTTP_401_UNAUTHORIZED, "UNAUTHORIZED"
        ),
        ExceptionHandlerConfig(
            ConnectionError,
            status.HTTP_503_SERVICE_UNAVAILABLE,
            "CONNECTION_ERROR",
            "Database connection failed",
            True,
        ),
        ExceptionHandlerConfig(
            TransactionError,
            status.HTTP_409_CONFLICT,
            "TRANSACTION_ERROR",
            "Database transaction failed",
            True,
        ),
        ExceptionHandlerConfig(
            DatabaseError,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "DATABASE_ERROR",
            "Database operation failed",
            True,
        ),
        ExceptionHandlerConfig(
            SQLAlchemyError,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "DATABASE_ERROR",
            "An unexpected database error occurred",
            True,
        ),
        ExceptionHandlerConfig(StarletteHTTPException, None, "HTTP_ERROR"),
        ExceptionHandlerConfig(
            BlogException,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "APPLICATION_ERROR",
            log=True,
        ),
        ExceptionHandlerConfig(
            Exception,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "INTERNAL_SERVER_ERROR",
            "An unexpected error occurred",
            True,
        ),
    ]

    for config in exception_handlers:

        async def handler(
            request: Request, exc: Exception, config: ExceptionHandlerConfig = config
        ) -> JSONResponse:
            """Generic exception handler using config dataclass."""
            if config.log:
                logger.error(f"{config.exc_class.__name__}: {exc}", exc_info=exc)

            status_code = config.status_code or getattr(
                exc, "status_code", status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            message = config.default_message or str(exc)

            details = getattr(exc, "details", None)
            if hasattr(exc, "validation_errors"):
                details = {"errors": exc.validation_errors}
            elif hasattr(exc, "errors"):
                details = {"errors": exc.errors()}

            return create_error_response(
                status_code=status_code,
                error_type=config.error_type,
                message=message,
                details=details,
            )

        app.add_exception_handler(config.exc_class, handler)
