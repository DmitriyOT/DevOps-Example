# DevOps Example — DevOps Test Task

![CI](https://github.com/DmitriyOT/DevOps-Example/actions/workflows/ci.yml/badge.svg)

[Русская версия](README.ru.md)

A simple Python web application with an nginx reverse proxy, deployed in Docker containers using Docker Compose.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## Architecture

```
User
    │
    ▼
http://localhost:80  (host port)
    │
    nginx (container devops-example-nginx)
    │
    ▼ proxy_pass → http://backend:8080
    backend (container devops-example-backend)
```

- **backend** — a Python HTTP server (`http.server`), listens on port `8080`, reachable only inside the Docker network.
- **nginx** — the official nginx image, accepts HTTP requests on port `80` and proxies them to the backend.
- The services communicate over the internal Docker network `devops-example-network` via service names.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Build and start the containers:

   ```bash
   docker compose up -d --build
   ```

3. Make sure the containers are running:

   ```bash
   docker compose ps
   ```

## How to Verify the Result

Send a request to nginx:

```bash
curl http://localhost
```

Expected response:

```
Hello from DevOps Example!
```

## Stopping and Removing Containers

```bash
docker compose down
```

If you also need to remove the built images:

```bash
docker compose down --rmi local
```

## Technologies Used

- Python 3.12 (official `python:3.12-alpine` image)
- nginx 1.27 (official `nginx:1.27-alpine` image)
- Docker / Docker Compose
- GitHub Actions (CI)

## CI

On every push to `main` and on every pull request, a pipeline
(`.github/workflows/ci.yml`) runs that:

1. Builds the Docker images (`docker compose build`).
2. Brings up the whole stack (`docker compose up -d`).
3. Runs a smoke test: a request through nginx must return `Hello from DevOps Example!`.
4. Verifies that the backend is not reachable from the host directly (only through nginx).
