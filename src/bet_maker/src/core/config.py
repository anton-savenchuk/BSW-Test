from functools import lru_cache

from pydantic import AmqpDsn, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    TIMEDELTA: int

    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        extra="ignore",
        validate_assignment=True,
        case_sensitive=True,
        env_prefix="BETMAKER_",
        env_file=".env",
        env_file_encoding="utf-8",
    )


class OverallSettings(BaseSettings):
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int

    RABBITMQ_EXCHANGE: str
    RABBITMQ_QUEUE: str
    RABBITMQ_EXCHANGE_TYPE: str
    RABBITMQ_ROUTING_KEY: str

    RABBITMQ_CELERY_QUEUE: str

    @property
    def RABBITMQ_URL(self) -> AmqpDsn:
        return f"amqp://{self.RABBITMQ_DEFAULT_USER}:{self.RABBITMQ_DEFAULT_PASS}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}//"

    model_config = SettingsConfigDict(
        extra="ignore",
        validate_assignment=True,
        case_sensitive=True,
        env_prefix="OVERALL_",
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_overall_settings() -> OverallSettings:
    return OverallSettings()


settings = get_settings()
overall_settings = get_overall_settings()
