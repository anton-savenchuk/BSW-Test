from celery import Celery

from src.core.config import overall_settings


celery_app = Celery(
    "tasks",
    broker=overall_settings.RABBITMQ_URL,
    include=["src.tasks.tasks"],
)

celery_app.conf.update(
    task_default_queue=overall_settings.RABBITMQ_CELERY_QUEUE,
    task_default_exchange=overall_settings.RABBITMQ_EXCHANGE,
    task_default_exchange_type=overall_settings.RABBITMQ_EXCHANGE_TYPE,
    task_default_routing_key=overall_settings.RABBITMQ_ROUTING_KEY,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)