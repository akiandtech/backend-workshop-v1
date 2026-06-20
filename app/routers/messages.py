"""Messages endpoints.

This lesson is about reading values from the URL:
- a PATH parameter:  /messages/{category}
- a QUERY parameter: /messages/{category}?length=5

The messages themselves live in a JSON file (app/data/messages.json) so we can
focus on the routing, not on a database (that comes later).
"""

import json
from pathlib import Path
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.utils.errors import generate_error_response

router = APIRouter()

# The categories we support. The "gay lingo" key has a space, which is fine in
# JSON and in a URL (it becomes "gay%20lingo" when typed in the browser).
VALID_CATEGORIES = ["funny", "inspirational", "facts", "conyo", "gay lingo"]

# Build an absolute path to the data file so it loads no matter where the app is
# started from. __file__ is this file; .parent.parent walks up to the app/ folder.
DATA_PATH = Path(__file__).parent.parent / "data" / "messages.json"


def load_messages() -> dict:
    """Read and return all messages from the JSON file."""
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


class GroupedMessages(BaseModel):
    """All messages, grouped by category.

    "gay lingo" is not a valid Python attribute name (it has a space), so we use
    a field alias. FastAPI serializes back to "gay lingo" in the JSON response.
    """

    funny: list[str]
    inspirational: list[str]
    facts: list[str]
    conyo: list[str]
    gay_lingo: list[str] = Field(alias="gay lingo")


class CategoryMessages(BaseModel):
    """Messages for a single category, plus a count."""

    category: str
    count: int
    messages: list[str]


@router.get("/messages", response_model=GroupedMessages)
def get_all_messages():
    """Return all 125 messages, grouped by category."""
    return load_messages()


@router.get("/messages/{category}")
def get_messages_by_category(category: str, length: Optional[int] = None):
    """Return messages for one category.

    - category (path param): must be one of VALID_CATEGORIES, else 404.
    - length (query param):
        * omitted        -> return all 25 messages
        * 1..25          -> return that many
        * greater than 25 -> 400
        * 0 or negative  -> 400
    """
    data = load_messages()

    if category not in VALID_CATEGORIES:
        return generate_error_response(
            404, f"Category '{category}' not found. Valid categories: {VALID_CATEGORIES}."
        )

    messages = data[category]

    if length is None:
        selected = messages
    elif length < 1:
        return generate_error_response(400, "length must be at least 1.")
    elif length > 25:
        return generate_error_response(400, "length cannot be greater than 25.")
    else:
        selected = messages[:length]

    return CategoryMessages(category=category, count=len(selected), messages=selected)
