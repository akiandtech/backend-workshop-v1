# Challenge 3 — Design your own request body

In the lesson you built `POST /tasks` with a `TaskCreate` schema and a custom
validator on `title`. Now design a request body of your own.

## Your task

Create a new, for-fun `POST` endpoint whose request body uses a **mix of data
types**. Your Pydantic schema must include **all** of the following:

- at least one **string** field
- at least one **integer** field
- at least one **boolean** field
- at least one **optional** field (one that can be left out)
- at least one field with a **custom validator** (`@field_validator`)

Pick a fun subject: a `Pet`, a `KaraokeSong`, a `MerchOrder`, a `Barkada` event —
anything you like.

## Requirements

1. Create a new schema file under `app/schemas/` (e.g. `app/schemas/pet.py`).
2. Create a new router file under `app/routers/` and register it in
   [app/main.py](app/main.py).
3. Use a Pydantic response model for the successful response.
4. Use the **shared error-response system** for any error you raise yourself:

   ```python
   from app.utils.errors import generate_error_response
   ```

## Example shape to aim for

```python
class Pet(BaseModel):
    name: str                       # string
    age_in_months: int              # integer
    vaccinated: bool                # boolean
    nickname: Optional[str] = None  # optional

    @field_validator("age_in_months")
    @classmethod
    def age_must_be_positive(cls, value: int) -> int:
        if value < 0:
            raise ValueError("age_in_months cannot be negative")
        return value
```

## Things to think about

- What does FastAPI return automatically when a field fails validation? (Try
  sending bad data and watch for the `422` response.)
- A custom validator runs *after* the basic type check. Why is that useful?

## Stretch goal

Add a `model_validator` (instead of a `field_validator`) that checks **two
fields together** — for example, "if `is_on_sale` is true, then `sale_price`
must be provided."
