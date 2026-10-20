# Evaluation rubric

| Area | Weight | What is checked |
| --- | ---: | --- |
| Aggregation logic | 40 | Portion scaling, merging, units, synonyms, inventory subtraction |
| Contract and data quality | 30 | Recipe v1 compatibility, validation, errors, API documentation |
| Delivery quality | 30 | Tests, reproducible launch, documentation, security hygiene |

## Acceptance checklist

- [ ] `POST /aggregate` accepts one to twenty valid Recipe v1 objects.
- [ ] Equivalent ingredients are merged without losing a source reference.
- [ ] Mass and volume units are normalized with documented conversion rules.
- [ ] A unit cannot be converted only when a safe conversion is known.
- [ ] Portion scaling uses the Recipe servings value.
- [ ] Invalid input produces a structured 4xx error.
- [ ] Tests cover happy path, invalid input, conversion and matching edge cases.
- [ ] Local start and Docker start are documented and repeatable.

## Review roles

Victoria Pugach checks contracts. Lyuba Novokhatskaya checks security. Both check the pipeline and tests. If their scores differ by more than 10%, they perform a joint review before the result is finalized.
