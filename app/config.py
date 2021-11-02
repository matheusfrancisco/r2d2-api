try:
    import unzip_requirements
except ImportError:
    Exception("there was a problem with imports")

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "R2D2-Recommendation-System"
    DEBUG: bool = False
    API_KEY: str = "Mock"
    BASE_ID: str = "Mock"

    class Config:
        env_file = ".env"


settings = Settings()
