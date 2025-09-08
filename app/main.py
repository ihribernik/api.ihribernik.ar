from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.config import Config
from app.infrastructure.web.middlewares.error import add_error_handlers
from app.infrastructure.web.middlewares.health import db_health_check_middleware
from app.infrastructure.web.routes import register_routes

load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Blog API",
        version="1.0.0",
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    config = Config()

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Health Check Middleware
    app.middleware("http")(db_health_check_middleware)

    # Database setup (if needed, e.g., create tables)
    # Example: Base.metadata.create_all(bind=engine)

    register_routes(app)

    add_error_handlers(app)

    return app


app = create_app()
