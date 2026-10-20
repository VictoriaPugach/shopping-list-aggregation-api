# API reference

Базовый адрес локального сервиса: `http://localhost:8001`. Swagger UI доступен по `/docs`.

## GET /health

Возвращает доступность API и версию общего контракта Recipe.

```json
{"status": "ok", "recipe_contract_version": "1.0.0"}
```

## POST /aggregate

Принимает JSON-объект с непустым массивом `recipes` из общего контракта. Максимум 20 рецептов на запрос.

```bash
curl -X POST http://localhost:8001/aggregate \
  -H 'Content-Type: application/json' \
  -d @data/aggregate-request.json
```

Целевой успешный ответ: `200 OK` с объектом `ShoppingList`. Некорректный JSON или Recipe: `422`. Каркас до реализации агрегации возвращает `501 aggregation_not_implemented`; после реализации этот ответ следует заменить документированными ошибками нормализации и входных данных.
