"""Tasks endpoints.

This lesson introduces the REQUEST BODY: data the client sends in the body of a
POST request (as JSON), which FastAPI validates against a Pydantic schema.

For now there is no database yet, so the endpoint simply echoes back the data it
received. We add real storage in a later lesson.
"""

from fastapi import APIRouter

from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    """Accept a task in the request body and return it back.

    Because the parameter is typed as TaskCreate, FastAPI:
      1. reads the JSON request body,
      2. validates it against the schema (rejecting bad data with a 422),
      3. hands us a ready-to-use TaskCreate object.
    """
    return task
