from fastapi import APIRouter

from src.bets.exceptions import BetCannotBePlace, BetCannotBeUpdated
from src.bets.schemas import BetCreateSchema, BetSchema, BetUpdateSchema
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


@router.patch("/update/")
async def update_bet(bet: BetUpdateSchema) -> BetSchema:
    "Bet update"

    updated_bet = await BetService.update_bet(bet)
    if not updated_bet:
        raise BetCannotBeUpdated

    return updated_bet
