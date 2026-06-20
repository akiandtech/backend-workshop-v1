"""Application entry point.

Run the app with:

    uvicorn app.main:app --reload

This lesson adds GLOBAL error handling. Instead of wrapping every route in its
own try/except, we register a handful of exception handlers in ONE place. When
anything goes wrong anywhere in the app, the matching handler turns it into our
standard error shape (see app/utils/errors.py). That is the DRY principle:
one definition of "what an error looks like," used everywhere.
"""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.routers import health, messages, tasks
from app.utils.errors import generate_error_response

# Create the FastAPI application.
app = FastAPI(title="Backend Workshop")


# --- Global error handlers -------------------------------------------------
# Each handler catches a type of error and returns our consistent ErrorResponse.


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Handle HTTP errors such as 404 Not Found for an unknown URL.

    FastAPI raises this when a path doesn't match any route (404), or when code
    raises HTTPException on purpose. We reshape it into our standard error body.
    """
    return generate_error_response(exc.status_code, str(exc.detail))


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle 422 errors when a request body fails Pydantic validation.

    By default FastAPI returns a detailed list here. We override it so the client
    always sees the same simple {code, message} shape as every other error.
    """
    return generate_error_response(
        422, "Validation error: the request data is invalid."
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """Catch-all for any unexpected error: returns 500 Internal Server Error.

    This is the safety net. If something we didn't anticipate blows up, the
    client still gets a clean error instead of a raw stack trace.
    """
    return generate_error_response(
        500, "Internal server error. Please try again later."
    )


# --- Routers ---------------------------------------------------------------
# Register the routers so their endpoints are part of the app.
app.include_router(health.router)
app.include_router(messages.router)
app.include_router(tasks.router)
