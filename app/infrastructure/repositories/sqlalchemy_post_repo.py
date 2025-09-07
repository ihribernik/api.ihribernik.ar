from app.domain.models.post import Post
from app.domain.ports.post_repository import PostRepository
from app.infrastructure.database.models import Post
from app.infrastructure.database import db


class SqlAlchemyPostRepository(PostRepository):

    def save(self, post: Post) -> Post:
        post = Post(
            title=post.title,
            content=post.content,
            author=post.author,
        )
        db.session.add(post)
        db.session.commit()
        post.id = post.id
        return post

    def get_all(self):
        posts = db.session.execute(db.select(Post).order_by(Post.title)).scalars()
        return posts

    def get_by_id(self, post_id: int):
        return db.get_or_404(Post, post_id)
