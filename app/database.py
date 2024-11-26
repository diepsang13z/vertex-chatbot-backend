from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import settings

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    """Generator function for dependency injection to fetch a new session on a new request."""
    db = Session()
    try:
        yield db
    finally:
        db.close()
