"""
Shared test fixtures and configuration for all test types.
"""
from typing import Any, Dict, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from app.application.blog_service import BlogService
from app.domain.models.post import Post
from app.infrastructure.database import Base
from app.infrastructure.repositories.sqlalchemy_post_repo import (
    SqlAlchemyPostRepository,
)
from app.main import create_app

# Test database URL
TEST_DB_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")
def test_db_url() -> str:
    """Provide test database URL."""
    return TEST_DB_URL

@pytest.fixture(scope="session")
def test_engine() -> Generator[Engine, None, None]:
    """Create test database engine."""
    engine = create_engine(
        TEST_DB_URL,
        connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(test_engine: Engine) -> Generator[Session, None, None]:
    """Provide test database session."""
    connection = test_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def post_repository(db_session: Session) -> SqlAlchemyPostRepository:
    """Provide test post repository."""
    return SqlAlchemyPostRepository(db_session)

@pytest.fixture(scope="function")
def blog_service(post_repository: SqlAlchemyPostRepository) -> BlogService:
    """Provide test blog service."""
    return BlogService(post_repository)

@pytest.fixture(scope="function")
def test_app(db_session: Session) -> FastAPI:
    """Provide test FastAPI application."""
    app = create_app()

    # Override database session
    def override_get_db() -> Generator[Session, None, None]:
        try:
            yield db_session
        finally:
            pass

    from app.infrastructure.database import get_db
    app.dependency_overrides[get_db] = override_get_db

    return app

@pytest.fixture(scope="function")
def test_client(test_app: FastAPI) -> Generator[TestClient, None, None]:
    """Provide test client for FastAPI application."""
    with TestClient(test_app) as client:
        yield client

@pytest.fixture
def sample_post() -> Dict[str, Any]:
    """Provide sample post data."""
    return {
        "title": "Test Post",
        "content": "Test Content",
        "author": "test_author"
    }

@pytest.fixture
def sample_domain_post() -> Post:
    """Provide sample domain post."""
    return Post(
        title="Test Post",
        content="Test Content",
        author="test_author"
    )
