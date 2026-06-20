"""Application entry point.

Run the app with:

    uvicorn app.main:app --reload

New in this lesson: the database is created on startup. We use a "lifespan"
function — code that runs once when the app boots — to create all our tables
with SQLAlchemy's create_all(). This is the simplest possible "migration": no
extra tools, just "make sure the tables exist."
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database.db import Base, engine

# Importing the model registers it on Base.metadata, so create_all() knows about
# the 'tasks' table. (The 'noqa' tells linters the import is used on purpose.)
from app.database.models.task import Task  # noqa: F401
from app.routers import health, messages, tasks
from app.utils.errors import generate_error_response


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run startup/shutdown code. Here: create database tables on startup."""
    Base.metadata.create_all(bind=engine)
    yield
    # (Nothing to clean up on shutdown for this simple app.)


# Create the FastAPI application and attach the lifespan handler.
app = FastAPI(title="Backend Workshop", lifespan=lifespan)


# --- Global error handlers -------------------------------------------------
# Each handler catches a type of error and returns our consistent ErrorResponse.


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Handle HTTP errors such as 404 Not Found for an unknown URL."""
    return generate_error_response(exc.status_code, str(exc.detail))


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle 422 errors when a request body fails Pydantic validation."""
    return generate_error_response(
        422, "Validation error: the request data is invalid."
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """Catch-all for any unexpected error: returns 500 Internal Server Error."""
    return generate_error_response(
        500, "Internal server error. Please try again later."
    )


# --- Routers ---------------------------------------------------------------
# Register the routers so their endpoints are part of the app.
app.include_router(health.router)
app.include_router(messages.router)
app.include_router(tasks.router)
