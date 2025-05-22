from pydantic_settings import BaseSettings
from typing import Optional

class ETLSettings(BaseSettings):
    db_url: Optional[str] = None
    log_level: str = "INFO"
    # Add more settings as needed

    class Config:
        env_file = ".env"

settings = ETLSettings()
