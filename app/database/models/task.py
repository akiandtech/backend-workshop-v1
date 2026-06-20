"""The Task database model.

A SQLAlchemy model is a Python class that maps to a database TABLE. Each
attribute (Column) becomes a column in that table. This describes how a task is
stored on disk — not what the API accepts (that's the Pydantic schema's job).
"""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.database.db import Base


class Task(Base):
    """A single to-do task, stored in the 'tasks' table."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
