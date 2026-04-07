"""Application database."""

from collections.abc import Generator

from sqlalchemy import text
from sqlmodel import Session, create_engine

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)


def get_session() -> Generator[Session, None, None]:
    """Get sesstion."""
    with Session(engine) as session:
        yield session


def check_db_connection() -> bool:
    """Check database connection."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
