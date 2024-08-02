from pydantic_settings import BaseSettings
import logging
from pydantic import ValidationError

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Todo App"
    API_VERSION: str = "1.0.0"
    DATABASE_URL: str

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
