import asyncio
import json
import random

import aio_pika

from src.core.celery import celery_app
from src.core.rabbitmq import async_rabbitmq_connection
from src.events.schemas import (
    EventIDSchema,
    EventStateSchema,
    EventUpdateSchema,
)


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
    await update_event_state("event_states", event_id, event_new_state)


async def update_event_state(queue_name: str, event_id: EventIDSchema, event_state: EventStateSchema):
    async with async_rabbitmq_connection as connection:
        message = {
            "event_id": event_id,
            "state": event_state,
        }

        await connection.declare_queue(queue_name, durable=True)
        await connection.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message).encode()),
            routing_key=queue_name,
        )
