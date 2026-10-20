import argparse
import json
from pathlib import Path

from src import aggregator
from src.models import Recipe


def load_recipes(path: Path) -> list[Recipe]:
    """Accept either one Recipe object or the same request body as POST /aggregate."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "recipes" in payload:
        return [Recipe.model_validate(recipe) for recipe in payload["recipes"]]
    return [Recipe.model_validate(payload)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Fropti shopping list from Recipe JSON files")
    parser.add_argument("recipes", nargs="+", type=Path)
    args = parser.parse_args()
    try:
        recipes = [recipe for path in args.recipes for recipe in load_recipes(path)]
        result = aggregator.aggregate_recipes(recipes)
    except (OSError, ValueError, NotImplementedError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
