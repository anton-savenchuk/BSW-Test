import aiohttp

from core.exception import BaseHTTPException


class EventService:
    @staticmethod
    async def get_all_active():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("http://line_provider:8000/line-provider/events/") as response:
                    response.raise_for_status()
                    return await response.json()
        except Exception as e:
            raise BaseHTTPException from e
