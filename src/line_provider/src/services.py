from datetime import datetime, timedelta, timezone

from sqlalchemy import insert, select

from src.core.config import settings
from src.core.database import async_session_maker
from src.core.service import BaseService
from src.models import Event
from src.schemas import EventCreateSchema


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

    @classmethod
    async def create_event(cls, event: EventCreateSchema):
        async with async_session_maker() as session:
            min_time_before_event = (
                datetime.now(timezone.utc).replace(tzinfo=None)
                + timedelta(minutes=settings.TIMEDELTA)
            )
            if event.deadline >= min_time_before_event:
                stmt = (
                    insert(Event)
                    .values(**event.model_dump(exclude_unset=True))
                    .returning(Event)
                )
                new_event = await session.execute(stmt)
                if new_event:
                    await session.commit()

                    return new_event.scalar()
