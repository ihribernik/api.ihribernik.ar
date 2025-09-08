from fastapi.testclient import TestClient
from app.main import app

def test_create_and_list_posts():
    client = TestClient(app)
    # Create post
    response = client.post("/api/posts/", json={"title": "title", "content": "content", "author": "author"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "title"
    # List posts
    response = client.get("/api/posts/")
    assert response.status_code == 200
    posts = response.json()
    assert any(post["title"] == "title" for post in posts)
