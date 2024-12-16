import asyncio
import random

from src.core.celery import celery_app
from src.events.schemas import EventIDSchema, EventUpdateSchema


@celery_app.task
def complete_event(event_id: EventIDSchema):
    """The task for completing the event"""

    current_loop = asyncio.get_event_loop()
    current_loop.run_until_complete(complete_event_async(event_id))


async def complete_event_async(event_id: EventIDSchema):
    from src.events.services import EventService

    event_new_state = random.choice([2, 3])

    await EventService.update_event(
        EventUpdateSchema(
            **{
                "event_id": event_id,
                "state": event_new_state,
            }
        )
    )
