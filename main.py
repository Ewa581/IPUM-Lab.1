import argparse
import os

from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = f".env.{environment}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Env file {env_file} not found!")
    load_dotenv(env_file)  # Ładuje zmienne z pliku do środowiska


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load environment variables.")
    parser.add_argument(
        "--environment", type=str, default="dev", help="Environment (dev, test, prod)"
    )
    args = parser.parse_args()

    export_envs(args.environment)  # Ładuje .env.dev/.env.test/.env.prod

    settings = Settings()  # Czyta zmienne z środowiska
    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
