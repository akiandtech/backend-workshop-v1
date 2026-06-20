"""Pydantic schemas for tasks.

A "schema" describes the shape of data going INTO an endpoint (the request body)
or coming OUT of it (the response). FastAPI uses these to validate and document
your API automatically.
"""

from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    """The data a client must send to create a task.

    Field(...) lets us attach rules. FastAPI turns broken rules into a 422 error
    automatically, so we don't have to check these by hand.
    """

    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: bool = False

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        """Custom rule: a title of only spaces ("   ") is not allowed.

        min_length=1 alone would accept "   " because it has length 3. This
        validator strips the whitespace and rejects it if nothing is left.
        """
        stripped = value.strip()
        if not stripped:
            raise ValueError("title must not be blank")
        return stripped


class TaskResponse(BaseModel):
    """The data we send back after receiving a task.

    For now this just echoes what was sent. Later (once we add a database) we'll
    extend it with fields like id and created_at.
    """

    title: str
    description: Optional[str] = None
    completed: bool
