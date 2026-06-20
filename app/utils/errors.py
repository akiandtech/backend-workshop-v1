"""Shared error-response system.

Every error in this app should look the same to the client. Instead of writing a
different error shape in every route, we define the shape ONCE here and use a
single helper to build it. This is the DRY ("Don't Repeat Yourself") principle.
"""

from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """The one and only shape of an error response in this app.

    code:    the HTTP status code (e.g. 404, 400)
    message: a human-readable explanation of what went wrong
    """

    code: int
    message: str


def generate_error_response(code: int, message: str) -> JSONResponse:
    """Build a consistent JSON error response.

    Use this everywhere instead of hand-writing error payloads. It returns a
    JSONResponse with the given status code and our standard ErrorResponse body.
    """
    error = ErrorResponse(code=code, message=message)
    return JSONResponse(status_code=code, content=error.model_dump())
