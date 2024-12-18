from src.core.celery import celery_app


@celery_app.task
def update_event_state(data):
    """The task for update event state on bet"""

    print(data)
