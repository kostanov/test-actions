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

## Endpoint'ы

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/` | Корневой endpoint с подсказкой |
| GET | `/time` | Возвращает текущее время сервера в формате ISO 8601 |

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

## Документация API

После запуска сервера доступна интерактивная документация:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Требования

- Python >= 3.10
- FastAPI >= 0.115.0
- Uvicorn >= 0.32.0
