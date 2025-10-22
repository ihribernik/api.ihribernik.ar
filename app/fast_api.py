from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import Settings
from app.presentation.api.middlewares.error import add_error_handlers
from app.presentation.api.middlewares.health import db_health_check_middleware
from app.presentation.api.routes import register_routes

load_dotenv()


def create_app() -> FastAPI:
    settings = Settings()

    fastapi_app = FastAPI(
        title=settings.API_TITLE,
        version=settings.API_VERSION,
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    fastapi_app.middleware("http")(db_health_check_middleware)

    register_routes(fastapi_app, prefix=settings.API_PREFIX)

    add_error_handlers(fastapi_app)

    return fastapi_app


app = create_app()
