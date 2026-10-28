"""FastAPI application entrypoint."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name)


class QueryRequest(BaseModel):
    query: str = Field(min_length=1, max_length=10_000)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/query")
async def query(request: QueryRequest) -> dict[str, str]:
    raise HTTPException(
        status_code=503,
        detail="RAG pipeline and NeMo Guardrails are not configured yet.",
    )
