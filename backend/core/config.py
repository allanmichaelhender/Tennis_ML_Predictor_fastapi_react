from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import PostgresDsn, field_validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI Project"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str

    # Configuration to read the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignores other vars in .env not defined here
    )

    # List of origins allowed to make CORS requests
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    # Tells Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    @field_validator("DATABASE_URL")
    @classmethod
    def validate_postgres_url(cls, v: str) -> str:
        if v.startswith("postgres://"):
            return v.replace("postgres://", "postgresql://", 1)
        return v


settings = Settings()
