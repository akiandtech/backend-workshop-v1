# Challenge 4 — Your own custom exceptions

In the lesson you added global handlers for 404, 422, and 500 in
[app/main.py](app/main.py). Every handler returns the same `ErrorResponse`
shape. Now create your own exception types and let the global handler catch them.

## Your task

1. Define **at least two custom exception types**. A custom exception is just a
   class that inherits from `Exception`:

   ```python
   class TaskNotFoundError(Exception):
       def __init__(self, task_id: int):
           self.task_id = task_id

   class CategoryClosedError(Exception):
       pass
   ```

   (Put them wherever makes sense — e.g. a new `app/utils/exceptions.py`.)

2. **Register a global handler for each** in `app/main.py`, the same way the
   lesson registers the built-in ones:

   ```python
   @app.exception_handler(TaskNotFoundError)
   async def task_not_found_handler(request, exc):
       return generate_error_response(404, f"Task {exc.task_id} was not found.")
   ```

   Every handler **must** return `generate_error_response(...)` so the shape
   stays consistent.

3. **Trigger each exception on purpose** from one of the existing endpoints (or a
   new one) so you can prove the global handler catches it:

   ```python
   raise TaskNotFoundError(task_id)
   ```

## Requirements

- At least **two** new custom exception types.
- A **registered handler** for each one.
- Each exception is **actually raised** from an endpoint so you can see it work.
- All responses use the **shared error-response system** — no new error shapes.

## How to test (Thunder Client)

Hit the endpoint that raises your exception and confirm:
- the HTTP status code is what your handler set, and
- the response body is the familiar `{ "code": ..., "message": ... }`.

## Things to think about

- Why is raising a domain-specific exception (like `TaskNotFoundError`) cleaner
  than returning an error response in the middle of your business logic?
- The global handler means your route code can focus on the happy path and let
  the handler deal with the error shape. Where else could this simplify code?
