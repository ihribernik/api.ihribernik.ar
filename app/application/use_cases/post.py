from typing import List, Optional

from app.domain.models import Post
from app.domain.repositories.post import PostRepository


class CreatePost:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, title: str, content: str, slug: str) -> Post:
        post = Post(id=None, title=title, content=content, slug=slug)
        return self.repo.save(post)

class GetPostBySlug:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, slug: str) -> Optional[Post]:
        return self.repo.get_by_slug(slug)

class ListPosts:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self) -> List[Post]:
        return self.repo.list()
