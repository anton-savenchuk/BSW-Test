from fastapi import APIRouter

from src.bets.schemas import BetSchema
from src.bets.services import BetService


router = APIRouter(
    prefix="/bets",
    tags=["Bets"],
)


@router.get("/")
async def get_bets() -> list[BetSchema]:
    "All bets history"

    return await BetService.get_all()
