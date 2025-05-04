from pydantic import ValidationError, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        allowed_environments = {"dev", "test", "prod"}
        if value not in allowed_environments:
            raise ValueError(f"Environment must be one of: {allowed_environments}")
        return value


# Przykład użycia
if __name__ == "__main__":
    try:
        settings = Settings(ENVIRONMENT="dev", APP_NAME="Test App")
        print(settings)
    except ValidationError as e:
        print("Error:", e)
