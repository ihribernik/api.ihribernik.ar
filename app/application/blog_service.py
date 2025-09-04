from app.domain.models.post import Post
from app.domain.ports.post_repository import PostRepository

class BlogService:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def create_post(self, title: str, content: str, author: str) -> Post:
        post = Post(id=None, title=title, content=content, author=author)
        return self.repo.save(post)

    def list_posts(self):
        return self.repo.get_all()
