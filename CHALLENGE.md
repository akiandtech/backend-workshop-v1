# Challenge 2 — Your own path + query endpoint

In the lesson you built `/messages/{category}?length=N`, which reads a value from
the URL **path** and a value from the **query string**. Now build your own.

## Your task

Create a new, for-fun endpoint that uses **both**:

- at least one **path parameter** (part of the URL, like `/jokes/{topic}`)
- at least one **query parameter** (after the `?`, like `?count=3`)

Back it with **your own hardcoded JSON data file** (similar to
`app/data/messages.json`). Pick anything you find fun: jokes, recipes, song
lyrics, anime quotes, barangay trivia — your call.

## Requirements

1. Create a new JSON data file under `app/data/` (e.g. `app/data/jokes.json`).
2. Create a new router file under `app/routers/` (e.g. `app/routers/jokes.py`)
   and register it in [app/main.py](app/main.py).
3. Your endpoint must use a path parameter **and** at least one query parameter.
4. Use a Pydantic model for the successful response.
5. **Reuse the shared error-response system** for any validation error:

   ```python
   from app.utils.errors import generate_error_response

   return generate_error_response(404, "Topic not found.")
   ```

   Do **not** invent a new error shape. The whole point is that every error in
   the app looks the same.

## Ideas for validation

- Return `404` when the path parameter doesn't match any key in your data.
- Return `400` when a query parameter is out of range (too big, zero, negative).

## Stretch goal

Add a second query parameter (for example `?shuffle=true`) that changes the
order of the results.
