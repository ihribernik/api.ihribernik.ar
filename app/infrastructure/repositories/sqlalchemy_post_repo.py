from app.domain.models.post import Post
from app.domain.ports.post_repository import PostRepository
from app.infrastructure.db import SessionLocal
from app.infrastructure.db.models import PostModel

class SqlAlchemyPostRepository(PostRepository):
    def __init__(self):
        self.session = SessionLocal()

    def save(self, post: Post) -> Post:
        model = PostModel(
            title=post.title,
            content=post.content,
            author=post.author
        )
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        post.id = model.id
        return post

    def get_all(self):
        posts = self.session.query(PostModel).all()
        return [Post(id=p.id, title=p.title, content=p.content, author=p.author, created_at=p.created_at) for p in posts]

    def get_by_id(self, post_id: int):
        p = self.session.query(PostModel).get(post_id)
        if not p:
            return None
        return Post(id=p.id, title=p.title, content=p.content, author=p.author, created_at=p.created_at)
