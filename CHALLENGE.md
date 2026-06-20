# Challenge 5 — Add your own database model

In the lesson you added a `Task` model, a `TaskRepository` (with stub methods),
and had the table created on startup via `create_all()`. Now add a model of your
own.

> **Git first:** create your working branch from this challenge branch:
>
> ```bash
> git checkout challenge/5-database-integration
> git checkout -b my-challenge-5
> ```

## Your task

Create a brand-new database model of your choice. Ideas: `Note`, `Category`,
`Tag`, `Expense`, `Contact`.

## Requirements

1. **Define the SQLAlchemy model** with **at least 4 fields**. Follow the pattern
   in [app/database/models/task.py](app/database/models/task.py):

   ```python
   from sqlalchemy import Boolean, Column, DateTime, Integer, String
   from app.database.db import Base

   class Note(Base):
       __tablename__ = "notes"
       id = Column(Integer, primary_key=True, autoincrement=True)
       title = Column(String, nullable=False)
       body = Column(String, nullable=True)
       pinned = Column(Boolean, default=False)
       # ...at least 4 fields total
   ```

2. **Create a repository** for it (e.g. `app/database/repositories/note_repository.py`)
   with the same **5 method stubs** as `TaskRepository`:
   `get_all`, `get_by_id`, `create`, `update`, `delete`.

3. **Make sure the table is created on startup.** `create_all()` only knows about
   models that have been imported. Import your model in
   [app/main.py](app/main.py), exactly like `Task` is imported there:

   ```python
   from app.database.models.note import Note  # noqa: F401
   ```

## How to verify

Start the app once. SQLAlchemy will create your new table inside
`app/database/workshop.db`:

```bash
uvicorn app.main:app --reload
```

You can confirm the table exists with any SQLite viewer, or move on to
**challenge 6**, where you'll fill in those repository methods and build the
endpoints.

## Things to think about

- Why does `create_all()` need the model to be **imported** before it runs?
- What types make sense for your fields? (`String`, `Integer`, `Boolean`,
  `DateTime`...)

## Stretch goal

Add a `DateTime` field with a default of `datetime.utcnow`, like `created_at` on
the `Task` model, so each row records when it was created.
