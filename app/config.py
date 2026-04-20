from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    bot_token: str = ''
    admin_api_token: str = 'change-me'
    database_url: str = 'sqlite:///./data/app.db'
    log_level: str = 'INFO'
    teacher_password_salt: str = 'change-me'


@lru_cache
def get_settings() -> Settings:
    return Settings()
