import os
from pydantic import BaseSettings

# Settings
class Settings(BaseSettings):
    PROJECT_NAME: str = "TODO Backend"
    API_VERSION: str = "v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
