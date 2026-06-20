"""Application entry point.

Run the app with:

    uvicorn app.main:app --reload
"""

from fastapi import FastAPI

from app.routers import health

# Create the FastAPI application.
app = FastAPI(title="Backend Workshop")

# Register the health router so its endpoints are part of the app.
app.include_router(health.router)
