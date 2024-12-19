import asyncio
import json

from aio_pika import IncomingMessage

from src.core.config import overall_settings
from src.core.rabbitmq import async_rabbitmq_connection
from src.tasks.tasks import update_completed_event_state


async def handle_message(message: IncomingMessage):
    async with message.process():
        data = message.body.decode("utf-8")
        data: dict = json.loads(data)
        update_completed_event_state.delay(data.get("event_id"), data.get("state"))


async def consumer_run():
    async with async_rabbitmq_connection as channel:
        await channel.declare_exchange(
            overall_settings.RABBITMQ_EXCHANGE,
            overall_settings.RABBITMQ_EXCHANGE_TYPE,
            durable=True,
        )
        queue = await channel.declare_queue(
            overall_settings.RABBITMQ_CELERY_EVENT_STATE_QUEUE,
            durable=True,
        )
        await queue.consume(handle_message)

        try:
            await asyncio.Future()
        finally:
            await channel.close()


if __name__ == "__main__":
    asyncio.run(consumer_run())
