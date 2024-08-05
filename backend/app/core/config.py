import os
from pydantic_settings import BaseSettings


# Settings
class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str
    APP_NAME: str
    API_VERSION: str
    INTERNAL_DATABASE_URL: str
    DATABASE_URL: str

    class Config:
        env_file = "../.env"

settings = Settings()
