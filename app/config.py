try:
    import unzip_requirements
except ImportError:
    Exception("there was a problem with imports")

import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'R2D2'
    DEBUG: bool = False
    API_KEY: str = 'Mock'
    BASE_ID: str = 'Moc'

    class Config:
        env_file = ".env"


settings = Settings()
