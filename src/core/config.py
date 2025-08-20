import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.database_url: str = os.getenv(
            "DATABASE_URL", 
            "postgresql://postgres:postgres@localhost:5432/fastapi_db"
        )
        self.postgres_db: str = os.getenv("POSTGRES_DB", "fastapi_db")
        self.postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
        self.postgres_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")
        
        self.api_host: str = os.getenv("API_HOST", "0.0.0.0")
        self.api_port: int = int(os.getenv("API_PORT", "8000"))


settings = Settings()