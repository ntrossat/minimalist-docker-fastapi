## Generic single-database configuration with an async dbapi.

# Generate a new revision
```bash
alembic revision --autogenerate -m "Update DB"
```

# Updagre to the latest revision
```bash
alembic upgrade head
```

# Revert one revision
```bash
alembic downgrade -1
```


