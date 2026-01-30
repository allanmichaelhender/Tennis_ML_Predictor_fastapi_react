from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI Project"
    API_V1_STR: str = "/api/v1"
    
    # Example: postgresql+psycopg2://user:pass@localhost:5432/db
    DATABASE_URL: str = "sqlite:///./sql_app.db"
    
    # List of origins allowed to make CORS requests
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    # Tells Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
