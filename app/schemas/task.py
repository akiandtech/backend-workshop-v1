"""Pydantic schemas for tasks.

A "schema" describes the shape of data going INTO an endpoint (the request body)
or coming OUT of it (the response). FastAPI uses these to validate and document
your API automatically. These are separate from the SQLAlchemy model, which
describes how a task is stored in the database.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TaskCreate(BaseModel):
    """The data a client must send to CREATE a task."""

    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: bool = False

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        """A title of only spaces ("   ") is not allowed."""
        stripped = value.strip()
        if not stripped:
            raise ValueError("title must not be blank")
        return stripped


class TaskUpdate(BaseModel):
    """The data a client sends to UPDATE a task.

    Every field is optional: the client sends only the fields it wants to change.
    We reuse the same validation rules as TaskCreate where they apply.
    """

    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: Optional[bool] = None

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: Optional[str]) -> Optional[str]:
        """Same blank check as TaskCreate, but skip it when title is omitted."""
        if value is None:
            return value
        stripped = value.strip()
        if not stripped:
            raise ValueError("title must not be blank")
        return stripped


class TaskResponse(BaseModel):
    """The data we send back for a task.

    Now that tasks live in the database, the response includes the database-
    generated fields: id and created_at.

    from_attributes=True lets FastAPI build this straight from a SQLAlchemy Task
    object (reading task.id, task.title, ... directly).
    """

    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
