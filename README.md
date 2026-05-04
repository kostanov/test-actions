# Time Backend

Простой FastAPI бэкенд, возвращающий текущее время сервера.

## Установка

```bash
uv sync
```

## Запуск

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Использование с Docker

Сборка и запуск приложения с помощью Docker:

```bash
# Сборка образа
docker build -t time-backend .

# Запуск контейнера
docker run --rm -p 8000:8000 time-backend
```

После запуска сервер будет доступен на http://localhost:8000

## Endpoint'ы

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/` | Корневой endpoint с подсказкой |
| GET | `/time` | Возвращает текущее время сервера в формате ISO 8601 |
| GET | `/date` | Возвращает текущую дату сервера в формате ISO 8601 |

## Примеры ответов

**GET /**
```json
{
  "message": "Use /time endpoint to get current server time"
}
```

**GET /time**
```json
{
  "server_time": "2026-05-04T12:27:57.199233"
}
```

**GET /date**
```json
{
  "server_date": "2026-05-04"
}
```

## Документация API

После запуска сервера доступна интерактивная документация:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## CI/CD

Автоматическая сборка и деплой настроена через GitHub Actions (`.github/workflows/deploy.yml`):

### Процесс
1. При push в `main` запускается workflow
2. **Job `build`**: сборка Docker образа и пуш в GitHub Container Registry (GHCR)
3. **Job `deploy`**: SSH подключение к серверу, скачивание образа и запуск контейнера

### Необходимые секреты

В настройках репозитория (Settings → Secrets and variables → Actions) добавь:

| Секрет | Описание |
|--------|----------|
| `SSH_HOST` | IP или домен сервера |
| `SSH_USER` | Имя пользователя для SSH |
| `SSH_KEY` | Приватный SSH ключ (PEM формат) |
| `SSH_PORT` | Порт SSH (опционально, по умолчанию 22) |

### Подготовка сервера

На сервере должен быть установлен Docker и добавлен публичный ключ:

```bash
# Установка Docker
curl -fsSL https://get.docker.com | sh

# Добавление публичного ключа в authorized_keys
echo "<публичный_ключ>" >> ~/.ssh/authorized_keys
```

## Требования

- Python >= 3.10
- FastAPI >= 0.115.0
- Uvicorn >= 0.32.0
