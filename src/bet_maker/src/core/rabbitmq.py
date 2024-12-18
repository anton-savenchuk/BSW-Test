import aio_pika

from src.core.config import overall_settings


class AsyncRabbitMQConnection:
    def __init__(self, uri: str):
        self.uri = uri
        self.connection = None
        self.channel = None

    async def __aenter__(self):
        self.connection = await aio_pika.connect_robust(self.uri)
        self.channel = await self.connection.channel()
        return self.channel

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.channel:
            await self.channel.close()
        if self.connection:
            await self.connection.close()


async_rabbitmq_connection = AsyncRabbitMQConnection(overall_settings.RABBITMQ_URL)
