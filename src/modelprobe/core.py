"""Helpers for reading declared model capabilities."""


def capabilities(model: dict) -> set[str]:
    """Return normalized capability names declared by a model record."""
    values = model.get("capabilities", [])
    if isinstance(values, str):
        values = values.split(",")
    return {str(value).strip().casefold() for value in values if str(value).strip()}
