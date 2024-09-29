## FastAPI Docker Boilerplate

This repository provides a basic boilerplate for building FastAPI applications with Docker.

## Features

- FastAPI application with basic endpoints
- Dockerfile for building and running the application
- Docker Compose for managing the application and dependencies

## Getting Started

1. Install repository:
```bash
git clone https://github.com/your-username/fastapi-docker-boilerplate.git
```

2. Install dependencies:
```bash
pipenv install
```

3. Build and Run the Docker:
```bash
docker compose run --build
```

4. Access the application at `http://localhost:8000`.

## Usage

The `main.py` file contains the FastAPI application code. You can modify this file to add your own endpoints and logic.

The `Dockerfile` defines the Docker image for the application. You can modify this file to add additional dependencies or configurations.

The `compose.yml` file defines the Docker Compose configuration for the application. You can modify this file to add additional services or configurations.