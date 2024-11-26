import os
from pydantic_settings import BaseSettings

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ENV_TYPE = os.getenv('ENV_TYPE', 'dev')


class BaseConfig(BaseSettings):
    ENVIRONMENT: str = 'base'
    SECRET_KEY: str = os.getenv('SECRET_KEY', '')
    DEBUG: bool = bool(int(os.getenv('DEBUG', 0)))


class DevelopmentConfig(BaseConfig):
    ENVIRONMENT: str = 'dev'
    POSTGRES_URL: str = os.getenv('DEV_POSTGRES_URL', '')


class ProductionConfig(BaseConfig):
    ENVIRONMENT: str = 'prod'
    POSTGRES_URL: str = os.getenv('PROD_POSTGRES_URL', '')


def get_config(env_type: str) -> dict:
    '''Convert configs class to dict.'''
    export_config_list = [
        DevelopmentConfig,
        ProductionConfig,
    ]
    cfg_class_map = {
        cfg().ENVIRONMENT: cfg()
        for cfg in export_config_list
    }
    return cfg_class_map[env_type]


settings: dict = get_config(ENV_TYPE)
