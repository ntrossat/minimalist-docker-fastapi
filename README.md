## Minimalist FastAPI Template

This repository provides a simple and minimalist template to quickly build async FastAPI microservices.

## Features

- **FastAPI** application with basic endpoints
- **Docker** for building and running the application
- **PostgreSQL** to host your data
- **Poetry** for dependencies


## Getting Started

1. Install repository:
```bash
git clone git@github.com:ntrossat/minimalist-fastapi.git
```

2. Open the folder:
```bash
cd minimalist-fastapi
```

2. Copy the configuration file:
```bash
cp .env.example .env
```

3. Build and Run the Docker:
```bash
docker compose up --build
```

4. Access the application at `http://localhost:8000`.

