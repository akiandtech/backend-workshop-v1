# Backend Workshop

A beginner-friendly, 2-hour workshop that builds a small FastAPI backend step by
step. Each concept lives on its own branch so you can follow along, compare your
work, and jump to any point in the lesson.

The stack is intentionally small: **FastAPI**, **SQLite**, **SQLAlchemy**, and
**Pydantic**. No authentication, no heavy frameworks — just the core ideas you
need to build a real API.

## How the repo is organized

Every topic has two branches:

- A **`lesson/*`** branch contains the finished, working code for that topic.
  Lesson branches build on top of each other, so each one includes everything
  from the lessons before it.
- A **`challenge/*`** branch contains only a `CHALLENGE.md` file with an exercise
  for you to complete on your own, reusing what the matching lesson taught.

## Branches

| Branch | What it covers |
| ------ | -------------- |
| `main` | Project intro, requirements, and this guide. |
| `lesson/1-health-check` | First FastAPI app: a `GET /healthz` endpoint with a Pydantic response model. |
| `challenge/1-health-check` | Add your own fields (version, environment, uptime…) to the health response. |
| `lesson/2-path-query-params` | Path and query parameters via a `/messages` API, plus the shared error-response system. |
| `challenge/2-path-query-params` | Build a for-fun endpoint that uses a path param **and** a query param. |
| `lesson/3-request-body` | Request bodies validated with Pydantic schemas and a custom validator. |
| `challenge/3-request-body` | Design a request body that mixes strings, ints, booleans, optionals, and a validator. |
| `lesson/4-middlewares` | Global error handling with FastAPI exception handlers (DRY error shape). |
| `challenge/4-middlewares` | Add custom exception types and register handlers for them. |
| `lesson/5-database-integration` | SQLite + SQLAlchemy: engine, session dependency, `Task` model, repository stubs. |
| `challenge/5-database-integration` | Create your own model + repository and have its table created on startup. |
| `lesson/6-crud-endpoints` | Full CRUD for tasks: list, read, create, update, delete. |
| `challenge/6-crud-endpoints` | Implement full CRUD for the model you created in challenge 5. |

## Switching between branches

Use `git checkout` (or `git switch`) to move between branches:

```bash
# see every branch
git branch -a

# jump to a lesson
git checkout lesson/2-path-query-params

# jump to a challenge
git checkout challenge/2-path-query-params

# go back to the start
git checkout main
```

> Tip: follow the lessons in order (1 → 6). Each `lesson/*` branch already
> contains the code from the lessons before it.

## Running the app

```bash
# install the dependencies (see requirements.txt)
pip install -r requirements.txt

# start the server (from any lesson/* branch that has app/main.py)
uvicorn app.main:app --reload
```

Then open <http://127.0.0.1:8000/docs> for the interactive API docs, or use
[Thunder Client](https://www.thunderclient.com/) to send requests.
