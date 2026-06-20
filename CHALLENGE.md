# Challenge 6 — Full CRUD for your own model

This is the finale. In the lesson, `Task` got full CRUD: list, read one, create,
update, and delete. Now do the same for the model you built in **challenge 5**.

> **Git first:** this challenge continues your challenge-5 work. Create your
> branch from `challenge/5-database-integration` (where your model lives):
>
> ```bash
> git checkout challenge/5-database-integration
> git checkout -b my-challenge-6
> ```
>
> (If you already built challenge 5 on your own branch, continue from there.)

## Your task

Implement complete CRUD endpoints for your challenge-5 model (e.g. `Note`,
`Category`, `Tag`).

## Requirements

1. **Schemas** — create the Pydantic schemas for your model, following
   `app/schemas/task.py` as your guide:
   - a `Create` schema (required fields, with at least one custom validator),
   - an `Update` schema (all fields optional),
   - a `Response` schema (include `id` and any DB-generated fields, and set
     `model_config = ConfigDict(from_attributes=True)`).

2. **Repository** — fill in all **5 methods** of your repository (they were stubs
   in challenge 5):
   `get_all`, `get_by_id`, `create`, `update`, `delete`.

3. **Routes** — wire up the five endpoints in a new router and register it in
   `app/main.py`:

   | Method | Path | Behavior |
   | ------ | ---- | -------- |
   | GET    | `/your-things`           | list all |
   | GET    | `/your-things/{id}`      | one, or `404` |
   | POST   | `/your-things`           | create, return `201` |
   | PUT    | `/your-things/{id}`      | update, or `404` |
   | DELETE | `/your-things/{id}`      | delete, `204`, or `404` |

4. **Errors** — every error response must use the **shared error-response
   system**:

   ```python
   from app.utils.errors import generate_error_response
   return generate_error_response(404, "Not found.")
   ```

5. Use **appropriate HTTP status codes** (201 for create, 204 for delete, 404 for
   not found).

## How to test (Thunder Client)

Walk the full lifecycle:
1. `POST` a new item — confirm `201` and that it comes back with an `id`.
2. `GET` the list — confirm your item is there.
3. `GET /your-things/{id}` — confirm `200`; try a missing id for `404`.
4. `PUT` to change a field — confirm the change; try a missing id for `404`.
5. `DELETE` it — confirm `204`; delete again for `404`.

## Things to think about

- Why split the logic between the **router** (HTTP concerns) and the
  **repository** (database concerns)?
- Why use `exclude_unset=True` when applying an update, instead of overwriting
  every field?

Finish this and you've built a complete, validated, database-backed REST API —
nice work! 🎉
