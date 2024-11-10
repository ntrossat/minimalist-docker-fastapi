## Generic single-database configuration with an async dbapi.

# Generate a new revision
```bash
poetry run alembic revision --autogenerate -m "Update DB"
```

# Updagre to the latest revision
```bash
poetry run alembic upgrade head
```

# Revert one revision
```bash
poetry run alembic downgrade -1
```


