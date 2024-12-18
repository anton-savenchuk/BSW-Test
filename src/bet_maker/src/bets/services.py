from datetime import datetime, timezone

from sqlalchemy import insert

from src.bets.exceptions import BetNotFound
from src.bets.models import Bet
from src.bets.schemas import BetCreateSchema, BetUpdateSchema
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

    @classmethod
    async def update_bet(cls, bet: BetUpdateSchema):
        async with async_session_maker() as session:
            updated_bet = await session.get(Bet, bet.bet_id)
            if not updated_bet:
                raise BetNotFound

            updated_bet_data = bet.model_dump(exclude_unset=True)

            for field, value in updated_bet_data.items():
                setattr(updated_bet, field, value)

            await session.commit()

            return updated_bet
