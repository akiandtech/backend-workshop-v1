"""Repository for Task database operations.

A "repository" is a small class whose only job is to talk to the database for one
kind of thing (here, tasks). Keeping every database query in one place keeps the
route handlers clean and easy to read.

In lesson 5 these methods were stubs. Here we implement them fully.
"""

from sqlalchemy.orm import Session

from app.database.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    """All database access for tasks lives here."""

    def __init__(self, db: Session):
        # The repository holds the session it was given so every method can use it.
        self.db = db

    def get_all(self) -> list[Task]:
        """Return a list of every task in the database."""
        return self.db.query(Task).all()

    def get_by_id(self, task_id: int) -> Task | None:
        """Return a single task by its id, or None if it doesn't exist."""
        return self.db.query(Task).filter(Task.id == task_id).first()

    def create(self, data: TaskCreate) -> Task:
        """Create and save a new task, then return it (with its new id)."""
        task = Task(
            title=data.title,
            description=data.description,
            completed=data.completed,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)  # reload so we get the database-generated id/created_at
        return task

    def update(self, task_id: int, data: TaskUpdate) -> Task | None:
        """Update an existing task and return it, or None if not found."""
        task = self.get_by_id(task_id)
        if task is None:
            return None

        # exclude_unset=True means we only touch the fields the client actually sent.
        updates = data.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(task, field, value)

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task_id: int) -> bool:
        """Delete a task; return True if it was deleted, False if not found."""
        task = self.get_by_id(task_id)
        if task is None:
            return False

        self.db.delete(task)
        self.db.commit()
        return True
