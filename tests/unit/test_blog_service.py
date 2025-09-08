import pytest
from app.domain.models.post import Post
from app.application.blog_service import BlogService

class InMemoryPostRepository:
    def __init__(self):
        self._posts = []
        self._id = 1

    def save(self, post: Post) -> Post:
        post.id = self._id
        self._id += 1
        self._posts.append(post)
        return post

    def get_all(self):
        return self._posts

    def get_by_id(self, post_id: int):
        for post in self._posts:
            if post.id == post_id:
                return post
        raise Exception("Post not found")

def test_create_and_list_posts():
    repo = InMemoryPostRepository()
    service = BlogService(repo)
    post = service.create_post("title", "content", "author")
    assert post.id == 1
    posts = service.list_posts()
    assert len(posts) == 1
    assert posts[0].title == "title"
