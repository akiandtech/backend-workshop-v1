# Challenge 1 — Make the health check richer

In the lesson, `GET /healthz` returns just a `status` and a `message`. Real
health checks usually report a bit more about the running service.

## Your task

Extend the `/healthz` endpoint so its response includes **additional fields of
your choice**. Ideas:

- `environment` — e.g. `"development"` or `"production"`
- `version` — e.g. `"1.0.0"`
- `uptime` — how long the server has been running (in seconds)

## Steps

1. Open [app/routers/health.py](app/routers/health.py).
2. Add your new fields to the `HealthResponse` Pydantic model.
3. Update the `health_check()` function so it returns values for those fields.
4. Run the app and call the endpoint to confirm your new fields show up:

   ```bash
   uvicorn app.main:app --reload
   ```

   Then open <http://127.0.0.1:8000/healthz> (or use Thunder Client).

## Things to think about

- Why is it useful for a health check to report the `version` of the code?
- How would you calculate `uptime`? (Hint: record a start time when the app
  boots, then subtract it from the current time.)
- The response model is the *contract* of your endpoint — adding a field to the
  model is what makes FastAPI include it in the documented response.

## Stretch goal

Add a field whose value is computed at request time (like `uptime`) rather than
hardcoded. This forces you to think about where that value comes from.
