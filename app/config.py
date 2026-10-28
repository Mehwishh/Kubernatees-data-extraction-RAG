"""Centralized environment-based application settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Production RAG"
    app_env: str = "development"
    log_level: str = "INFO"
    portkey_api_key: str | None = None
    groq_api_key: str | None = None
    google_api_key: str | None = None
    qdrant_url: str | None = None
    qdrant_api_key: str | None = None
    nemo_config_path: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()
