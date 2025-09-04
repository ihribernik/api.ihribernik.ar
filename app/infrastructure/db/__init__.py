import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

# Cargar .env
load_dotenv()

# Construir URL de conexión
DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@"
    f"{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/"
    f"{os.getenv('DATABASE_NAME')}"
)

# Engine y Session
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
