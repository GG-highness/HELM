from sqlalchemy import text
from sqlmodel import SQLModel, create_engine, Session

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def check_db_connection() -> bool:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
