from src.bets.models import Bet
from src.core.service import BaseService


class BetService(BaseService):
    model = Bet
