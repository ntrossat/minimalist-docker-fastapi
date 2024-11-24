## Generic single-database configuration with an async dbapi.

# Generate a new revision
```bash
uv run alembic revision --autogenerate -m "Update DB"
```

# Updagre to the latest revision
```bash
uv run alembic upgrade head
```

# Revert one revision
```bash
uv run alembic downgrade -1
```


