import os, sys

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



# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])
