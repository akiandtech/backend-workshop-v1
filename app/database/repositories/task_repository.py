"""Repository for Task database operations.

A "repository" is a small class whose only job is to talk to the database for one
kind of thing (here, tasks). Keeping every database query in one place keeps the
route handlers clean and easy to read.

In THIS lesson the methods are just stubs (they do nothing yet). We implement
them fully in lesson 6, once we've seen how the model and session fit together.
"""

from sqlalchemy.orm import Session


class TaskRepository:
    """All database access for tasks lives here."""

    def __init__(self, db: Session):
        # The repository holds the session it was given so every method can use it.
        self.db = db

    def get_all(self):
        """Return a list of every task in the database."""
        pass

    def get_by_id(self, task_id):
        """Return a single task by its id, or None if it doesn't exist."""
        pass

    def create(self, data):
        """Create and save a new task, then return it."""
        pass

    def update(self, task_id, data):
        """Update an existing task and return it, or None if not found."""
        pass

    def delete(self, task_id):
        """Delete a task; return True if it was deleted, False if not found."""
        pass
