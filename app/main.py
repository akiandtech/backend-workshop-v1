"""Application entry point.

Run the app with:

    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.routers import health, messages

# Create the FastAPI application.
app = FastAPI(title="Backend Workshop")

# Register the routers so their endpoints are part of the app.
app.include_router(health.router)
app.include_router(messages.router)
