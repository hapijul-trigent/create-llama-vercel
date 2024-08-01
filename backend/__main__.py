from fastapi import FastAPI
from app.api.v1.endpoints import todos
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
)

app.include_router(items.router, prefix="/items", tags=["items"])
