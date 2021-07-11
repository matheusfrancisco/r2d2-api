from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "R2D2"
    DEBUG: bool = False


settings = Settings()
