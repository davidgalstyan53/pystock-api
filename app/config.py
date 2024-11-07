from typing import Optional, ClassVar
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_name: str = "Stock Market API"
    stock_api_key: Optional[str] = None

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(env_file=".env")
