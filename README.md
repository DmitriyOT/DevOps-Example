# DevOps Example — DevOps Test Task

Простое веб-приложение на Python с обратным прокси на nginx, развёрнутое в Docker-контейнерах через Docker Compose.

## Структура проекта

```
.
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## Архитектура

```
Пользователь
    │
    ▼
http://localhost:80  (порт хоста)
    │
    nginx (контейнер devops-example-nginx)
    │
    ▼ proxy_pass → http://backend:8080
    backend (контейнер devops-example-backend)
```

- **backend** — HTTP-сервер на Python (`http.server`), слушает порт `8080`, доступен только внутри Docker-сети.
- **nginx** — официальный образ nginx, принимает HTTP-запросы на порту `80`, проксирует их на backend.
- Взаимодействие между сервисами происходит по внутренней Docker-сети `devops-example-network` через имена сервисов.

## Требования

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Как запустить проект

1. Клонируйте репозиторий:

   ```bash
   git clone <URL-репозитория>
   cd <имя-репозитория>
   ```

2. Соберите и запустите контейнеры:

   ```bash
   docker compose up -d --build
   ```

3. Убедитесь, что контейнеры запущены:

   ```bash
   docker compose ps
   ```

## Как проверить результат

Выполните запрос к nginx:

```bash
curl http://localhost
```

Ожидаемый ответ:

```
Hello from DevOps Example!
```

## Остановка и удаление контейнеров

```bash
docker compose down
```

Если необходимо также удалить собранные образы:

```bash
docker compose down --rmi local
```

## Используемые технологии

- Python 3.12 (официальный образ `python:3.12-alpine`)
- nginx 1.27 (официальный образ `nginx:1.27-alpine`)
- Docker / Docker Compose
