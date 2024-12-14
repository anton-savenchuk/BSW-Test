from fastapi import APIRouter

from src.bets.exceprions import BetCannotBePlace
from src.bets.schemas import BetCreateSchema, BetSchema
from src.bets.services import BetService


router = APIRouter(
    prefix="/bets",
    tags=["Bets"],
)


@router.get("/")
async def get_bets() -> list[BetSchema]:
    "All bets history"

    return await BetService.get_all()


@router.post("/bet/{event_id}")
async def bet_event(bet: BetCreateSchema) -> BetSchema:
    "Bet by event ID"

    new_bet = await BetService.place_bet_event(bet)
    if not new_bet:
        raise BetCannotBePlace

    return new_bet
