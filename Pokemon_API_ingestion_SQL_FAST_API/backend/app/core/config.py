from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    app_name: str = "PokeAPI SQLite Challenge"
    backend_cors_origins: List[str] = ["http://localhost:5173"]

    class Config:
        env_file = ".env"


settings = Settings()
