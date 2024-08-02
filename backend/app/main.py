import os, sys, logging

# Add app to $PATH
# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the parent directory of the current file's directory to sys.path
sys.path.append('/opt/render/project/src/backend')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import todos
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from typing import AsyncGenerator

# Add backend directory to PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "..", ".."))

# Create all tables in the database
async def create_db_and_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup event
    await create_db_and_tables()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    lifespan=create_db_and_tables
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])
