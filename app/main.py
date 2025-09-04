from flask import Flask
from flask_cors import CORS
from flask_pydantic_spec import FlaskPydanticSpec

from app.infrastructure.config import Config
from app.infrastructure.web.middlewares.error import ErrorMiddleware
from app.infrastructure.web.middlewares.redoc import register_redoc
from app.infrastructure.web.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    ErrorMiddleware(app)

    register_routes(app)

    spec = FlaskPydanticSpec("flask", title="Blog API", version="1.0.0", openapi=True)
    spec.register(app)
    register_redoc(app, spec_url="/openapi.json", route="/redoc", title="Blog API Docs")

    return app


app = create_app()
