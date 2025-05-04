import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from settings import Settings


def test_settings_loading():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "Test App"
