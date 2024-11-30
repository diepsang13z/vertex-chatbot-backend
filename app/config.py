import os
from pydantic_settings import BaseSettings

from constants import ENVIRONMENT


class BaseConfig(BaseSettings):
    ENV: str = ENVIRONMENT.BASE
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')
    DEBUG: bool = bool(int(os.getenv('DEBUG', 0)))


class DevelopmentConfig(BaseConfig):
    ENV: str = ENVIRONMENT.DEVELOPMENT
    POSTGRES_URL: str = os.getenv('DEV_POSTGRES_URL', '')

    GEMINI_API_KEY: str = os.getenv('DEV_GEMINI_API_KEY', '')
    GEMINI_MODEL: str = os.getenv('DEV_GEMINI_MODEL', '')


class ProductionConfig(BaseConfig):
    ENV: str = ENVIRONMENT.PRODUCTION
    POSTGRES_URL: str = os.getenv('PROD_POSTGRES_URL', '')

    CORS_ORIGINS: list[str] = os.getenv('CORS_ORIGINS', []).split(',')
    CORS_METHODS: list[str] = os.getenv('CORS_METHODS', []).split(',')
    CORS_HEADERS: list[str] = os.getenv('CORS_HEADERS', []).split(',')
    CORS_CREDENTIALS: bool = bool(int(os.getenv('CORS_CREDENTIALS', 0)))

    GEMINI_API_KEY: str = os.getenv('PROD_GEMINI_API_KEY', '')
    GEMINI_MODEL: str = os.getenv('PROD_GEMINI_MODEL', '')


def get_config(env_type: str) -> dict:
    '''Convert configs class to dict.'''
    export_config_list = [
        DevelopmentConfig,
        ProductionConfig,
    ]
    cfg_class_map = {
        cfg().ENV: cfg()
        for cfg in export_config_list
    }
    return cfg_class_map[env_type]


ENV_TYPE = os.getenv('ENV_TYPE', 'dev')
settings: dict = get_config(ENV_TYPE)
