"""Database setup: engine, session, and the declarative Base.

This is the heart of our database layer. It does three things:
  1. creates the SQLAlchemy ENGINE (the connection to our SQLite file),
  2. creates a SESSION factory (each request gets its own session),
  3. defines BASE, the class our models inherit from.

We use SQLite, so the whole database is just a single file: workshop.db.
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# The database file lives next to this file, at app/database/workshop.db.
DB_PATH = Path(__file__).parent / "workshop.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# check_same_thread=False is needed for SQLite when used with a web server,
# because different requests may touch the connection from different threads.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# A session is how we read from and write to the database. SessionLocal() makes
# a new one. We open one per request and close it when the request is done.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Every model class (e.g. Task) inherits from Base. Base collects them so we can
# create all their tables at once with Base.metadata.create_all().
Base = declarative_base()


def get_db():
    """FastAPI dependency that hands a database session to a route.

    Use it in a route like this:

        @router.get("/tasks")
        def list_tasks(db: Session = Depends(get_db)):
            ...

    The 'yield' gives the session to the route; the 'finally' guarantees it is
    closed afterwards, even if the route raises an error.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
