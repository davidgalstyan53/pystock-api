from app.config import Settings


def test_default_api_name():
    settings = Settings()
    assert settings.api_name == settings.api_name
    assert settings.api_name != "Random API Name"


def test_env_api_name(monkeypatch):
    test_name = "Test API Name"
    monkeypatch.setenv("API_NAME", test_name)
    settings = Settings()
    assert settings.api_name == test_name
