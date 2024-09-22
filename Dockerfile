ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION} AS fastapi

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile* ./

RUN pip install --upgrade pip setuptools pipenv uvicorn
RUN pipenv install --dev

CMD ["pipenv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
