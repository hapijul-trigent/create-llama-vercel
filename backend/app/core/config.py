from pydantic_settings import BaseSettings
import logging, os
from pydantic import ValidationError

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Settings(BaseSettings):
    PROJECT_NAME: str
    API_VERSION: str
    DATABASE_URL: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: str

    class Config:
        env_file = ".env"

# Log environment variables for debugging
logging.debug("Environment Variables:")
for key, value in os.environ.items():
    logging.debug(f"{key}: {value}")

# Initialize settings
try:
    settings = Settings()
    logging.info("Settings loaded successfully")
except ValidationError as e:
    logging.error("Settings validation error: %s", e)
    raise e
