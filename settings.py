from pydantic_settings import BaseSettings
from pydantic import field_validator, ValidationError  # Zmienione importy

class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")  # Nowa składnia
    def validate_environment(cls, value):
        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(f"Environment must be one of: {allowed}")
        return value
