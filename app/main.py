from flask import Flask
from flask_cors import CORS
from flask_pydantic_spec import FlaskPydanticSpec

from app.infrastructure.db import db
from app.infrastructure.config import Config
from app.infrastructure.web.middlewares.error import ErrorMiddleware
from app.infrastructure.web.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    ErrorMiddleware(app)

    db.init_app(app)


    register_routes(app)

    spec = FlaskPydanticSpec("flask", title="Blog API", version="1.0.0", openapi=True)
    spec.register(app)

    return app


app = create_app()
