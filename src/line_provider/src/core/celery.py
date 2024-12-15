from celery import Celery

from src.core.config import settings


celery_app = Celery(
    "tasks",
    broker=settings.RABBITMQ_URL,
    include=["src.tasks.tasks"],
)

celery_app.conf.update(
    task_routes={
        "src.tasks.tasks": {"queue": "event-task"},
    },
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
