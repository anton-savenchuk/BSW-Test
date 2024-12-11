from datetime import datetime, timezone

from sqlalchemy import select

from src.core.database import async_session_maker
from src.core.service import BaseService
from src.models import Event


class EventService(BaseService):
    model = Event

    @classmethod
    async def get_all_active(cls):
        async with async_session_maker() as session:
            query = (
                select(Event)
                .where(
                    Event.deadline
                    > datetime.now(timezone.utc).replace(tzinfo=None)
                )
            )
            result = await session.execute(query)

            return result.scalars().all()
