ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION} AS dependencies

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Update package managers of the container
RUN pip install --upgrade pip poetry

# Install dependencies
COPY pyproject.toml .
RUN poetry install

# Apply migration to DB
FROM dependencies AS alembic
CMD ["poetry", "run", "alembic", "upgrade", "head"]

# Launch FastAPI
FROM dependencies AS fastapi
CMD ["poetry", "run", "fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "8000", "--reload"]