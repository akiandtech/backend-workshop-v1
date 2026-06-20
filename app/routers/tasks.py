"""Tasks endpoints — full CRUD.

CRUD = Create, Read, Update, Delete: the four basic things you do with stored
data. Each route asks for a database session via Depends(get_db), then hands the
real work to the TaskRepository. Errors use the shared error-response system so
every failure looks the same.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.utils.errors import generate_error_response

router = APIRouter()


@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    """READ all: return every task."""
    return TaskRepository(db).get_all()


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """READ one: return a single task, or 404 if it doesn't exist."""
    task = TaskRepository(db).get_by_id(task_id)
    if task is None:
        return generate_error_response(404, f"Task {task_id} not found.")
    return task


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    """CREATE: add a new task and return it with status 201 Created."""
    return TaskRepository(db).create(data)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    """UPDATE: change an existing task, or 404 if it doesn't exist."""
    task = TaskRepository(db).update(task_id, data)
    if task is None:
        return generate_error_response(404, f"Task {task_id} not found.")
    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """DELETE: remove a task. Returns 204 No Content, or 404 if not found."""
    deleted = TaskRepository(db).delete(task_id)
    if not deleted:
        return generate_error_response(404, f"Task {task_id} not found.")
    return None
