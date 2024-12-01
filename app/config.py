import os

from pydantic_settings import BaseSettings

from enums import Environment


class BaseConfig(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')
    DEBUG: bool = bool(int(os.getenv('DEBUG', 0)))


class DevelopmentConfig(BaseConfig):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    POSTGRES_URL: str = os.getenv('DEV_POSTGRES_URL', '')

    GEMINI_API_KEY: str = os.getenv('DEV_GEMINI_API_KEY', '')
    GEMINI_MODEL: str = os.getenv('DEV_GEMINI_MODEL', '')


class ProductionConfig(BaseConfig):
    ENVIRONMENT: Environment = Environment.PRODUCTION
    POSTGRES_URL: str = os.getenv('PROD_POSTGRES_URL', '')

    GEMINI_API_KEY: str = os.getenv('PROD_GEMINI_API_KEY', '')
    GEMINI_MODEL: str = os.getenv('PROD_GEMINI_MODEL', '')


def get_config(env: str):
    """Convert configs class to dict."""
    export_config_list = [
        DevelopmentConfig,
        ProductionConfig,
    ]

    cfg_class_map = {
        cfg().ENVIRONMENT: cfg()
        for cfg in export_config_list
    }

    return cfg_class_map[env]


env = Environment(os.getenv('ENV', Environment.DEVELOPMENT.name))
settings = get_config(env)
