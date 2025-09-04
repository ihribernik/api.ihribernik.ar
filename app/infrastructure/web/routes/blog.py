from flask import Blueprint, jsonify, request
from flask_pydantic import validate

from app.application.blog_service import BlogService
from app.infrastructure.repositories.sqlalchemy_post_repo import (
    SqlAlchemyPostRepository,
)
from app.schemas.post_schema import PostSchema

bp = Blueprint("blog", __name__)

repo = SqlAlchemyPostRepository()
service = BlogService(repo)


@bp.post("/posts")
@validate()
def create_post(body: PostSchema):
    data = request.json
    post = service.create_post(data["title"], data["content"], data["author"])
    return jsonify(post.__dict__), 201


@bp.get("/posts")
def list_posts():
    posts = service.list_posts()
    return jsonify([p.__dict__ for p in posts])
