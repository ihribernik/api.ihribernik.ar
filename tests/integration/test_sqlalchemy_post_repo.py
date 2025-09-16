import os
import tempfile
from typing import Generator
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.database.models import Post, Base
from app.infrastructure.mappers.post import PostMapper
from app.infrastructure.repositories.sqlalchemy.post import SqlAlchemyPostRepository
from sqlalchemy.orm import Session


@pytest.fixture
def session() -> Generator[Session, None, None]:
    db_fd, db_path = tempfile.mkstemp()
    engine = create_engine(f"sqlite:///{db_path}")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    os.close(db_fd)
    os.unlink(db_path)


def test_save_and_get_post(session: Session) -> None:
    repo = SqlAlchemyPostRepository(session)
    post_entity = Post(title="title", content="content", author="author")
    post = PostMapper.to_domain(post_entity)
    repo.save(post)
    posts = repo.get_all()
    assert len(posts) == 1
    assert posts[0].title == "title"
