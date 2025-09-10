from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.config import Settings
from app.infrastructure.middlewares.error import add_error_handlers
from app.infrastructure.middlewares.health import db_health_check_middleware
from app.infrastructure.routes import register_routes

load_dotenv()


def create_app() -> FastAPI:
    settings = Settings()

    app = FastAPI(
        title=settings.API_TITLE,
        version=settings.API_VERSION,
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.middleware("http")(db_health_check_middleware)

    register_routes(app, prefix=settings.API_PREFIX)

    add_error_handlers(app)

    return app


app = create_app()
