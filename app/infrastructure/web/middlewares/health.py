from typing import Callable

from fastapi import Request, Response
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.infrastructure.database import SessionLocal


async def db_health_check_middleware(request: Request, call_next: Callable) -> Response:
    """
    Middleware to check database health and add health headers to response.

    Args:
        request: FastAPI request
        call_next: Next middleware/route handler

    Returns:
        Response: FastAPI response with health check headers
    """
    is_health_check = request.url.path == "/health"
    is_db_healthy = True
    db_status = "available"

    try:
        if is_health_check:
            db = SessionLocal()
            try:
                # Quick query to check DB connection
                db.execute(text("SELECT 1"))
            except SQLAlchemyError as e:
                is_db_healthy = False
                db_status = str(e)
            finally:
                db.close()
    except Exception as e:
        is_db_healthy = False
        db_status = str(e)

    response: Response = await call_next(request)

    if is_health_check:
        response.headers["X-Database-Health"] = "ok" if is_db_healthy else "error"
        response.headers["X-Database-Status"] = db_status

    return response
