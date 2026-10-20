# Контракты данных

## Вход: Recipe 1.0.0

Входной контракт принадлежит пакету [`fropti-core-contracts`](https://github.com/VictoriaPugach/recipe-video-extraction-pipeline/tree/main/packages/fropti-core-contracts). Этот репозиторий не создаёт локальную копию `Recipe`; `src.models` импортирует его из пакета.

Для каждого рецепта обязательны `schema_version`, `title`, `servings`, `ingredients`, `steps` и `source`. Неизвестные порции и количества передаются как `null`. Допустимые единицы и правила версий определены в исходном пакете.

## Выход: ShoppingList

Это целевой контракт результата, который студент фиксирует вместе с реализацией:

```json
{
  "items": [
    {
      "name": "Яйца",
      "quantity": {"value": 6, "unit": "pcs"},
      "source_recipes": ["Омлет", "Блины"]
    }
  ],
  "unresolved": [
    {"name": "Соль", "reason": "quantity_unknown"}
  ]
}
```

Поля, обязательность, сортировка и правила отображения неизвестных значений должны быть согласованы до реализации и закреплены тестами. Не добавлять в `Recipe` остатки, цены, категории или внутренние ID только ради Shopping List API.
