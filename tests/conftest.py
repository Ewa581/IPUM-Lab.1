import pytest
from dotenv import load_dotenv


@pytest.fixture(autouse=True)
def load_test_env():
    load_dotenv(".env.test")
