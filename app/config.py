from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool = False
    API_KEY: str
    BASE_ID: str

    class Config:
        env_file = ".env"


settings = Settings()
