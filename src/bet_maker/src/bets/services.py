from datetime import datetime, timezone

from sqlalchemy import insert

from src.bets.models import Bet
from src.bets.schemas import BetCreateSchema
from src.core.database import async_session_maker
from src.core.service import BaseService
from src.events.schemas import EventSchema
from src.events.services import EventService


class BetService(BaseService):
    model = Bet

    @classmethod
    async def place_bet_event(cls, bet: BetCreateSchema):
        event: EventSchema = EventSchema(
            **await EventService.get_one(event_id=bet.event_id)
        )
        if (
            event.deadline >= datetime.now(timezone.utc).replace(tzinfo=None)
            and event.state == 1
        ):
            async with async_session_maker() as session:
                stmt = (
                    insert(Bet)
                    .values(**bet.model_dump(exclude_unset=True))
                    .returning(Bet)
                )
                new_bet = await session.execute(stmt)
                if new_bet:
                    await session.commit()

                    return new_bet.scalar()
