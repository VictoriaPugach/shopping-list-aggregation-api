from typing import Annotated

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

from src import aggregator
from src.config import MAX_RECIPES_PER_REQUEST
from src.models import CONTRACT_VERSION, Recipe

app = FastAPI(
    title="Fropti Shopping List API",
    version="0.1.0",
    description=f"Shopping-list aggregation scaffold. Recipe contract {CONTRACT_VERSION}.",
)


class AggregateRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recipes: Annotated[list[Recipe], Field(min_length=1, max_length=MAX_RECIPES_PER_REQUEST)]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "recipe_contract_version": CONTRACT_VERSION}


@app.post("/aggregate", responses={501: {"description": "Aggregation is not implemented"}})
def aggregate_shopping_list(request: AggregateRequest) -> dict:
    try:
        return aggregator.aggregate_recipes(request.recipes)
    except NotImplementedError as exc:
        raise HTTPException(
            status_code=501,
            detail={"code": "aggregation_not_implemented", "message": str(exc)},
        ) from exc
