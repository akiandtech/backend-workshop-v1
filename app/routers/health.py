"""Health check endpoint.

A health check is a simple endpoint that monitoring tools (or you) can call to
confirm the API is up and running.
"""

from fastapi import APIRouter
from pydantic import BaseModel

# A router groups related endpoints. We include it in main.py.
router = APIRouter()


class HealthResponse(BaseModel):
    """The shape of the JSON we send back from /healthz."""

    status: str
    message: str


@router.get("/healthz", response_model=HealthResponse)
def health_check():
    """Return a simple status so callers know the API is alive."""
    return HealthResponse(status="ok", message="API is up and running")
