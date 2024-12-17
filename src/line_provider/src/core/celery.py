from celery import Celery

from src.core.config import overall_settings


celery_app = Celery(
    "tasks",
    broker=overall_settings.RABBITMQ_URL,
    include=["src.tasks.tasks"],
)

celery_app.conf.update(
    task_default_queue="event-tasks",
    task_default_exchange="events",
    task_default_exchange_type="direct",
    task_default_routing_key="default",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
