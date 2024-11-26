from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import settings

SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    """
    Dependency injection generator that provides a new database session
    for each request.

    This ensures that a fresh session is created, used, and properly closed
    after the request is processed.
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
