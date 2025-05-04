from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = "test"  # Wartość domyślna
    APP_NAME: str = "Test App"  # Wartość domyślna
