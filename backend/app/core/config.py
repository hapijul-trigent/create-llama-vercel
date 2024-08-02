from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Todo App"
    API_VERSION: str = "1.0.0"
    DATABASE_URL: str = "postgresql://happy:3jsSJ38L8fRBIsjAc7w2flSYmWM2f7HF@dpg-cqm8m03qf0us73a7d7eg-a/tododb_ix00"

    class Config:
        env_file = ".env"

settings = Settings()
