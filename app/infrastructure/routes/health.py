from typing import Dict

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check(db: Session = Depends(get_db)) -> Dict[str, str | Dict[str, str]]:
    """
    Health check endpoint that verifies:
    - API is responsive
    - Database connection is working

    Returns:
        Dict with status information
    """
    db_status = "healthy"
    db_details = "connected"

    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError as e:
        db_status = "unhealthy"
        db_details = str(e)

    return {
        "status": "healthy" if db_status == "healthy" else "unhealthy",
        "database": {"status": db_status, "details": db_details},
    }
