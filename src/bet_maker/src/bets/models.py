from datetime import datetime

from sqlalchemy import DateTime, DECIMAL, text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class Bet(Base):
    __tablename__ = "bets"

    bet_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    event_id: Mapped[int] = mapped_column(
        nullable=False,
    )
    amount: Mapped[float] = mapped_column(
        DECIMAL(8, 2),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("TIMEZONE('utc', now())"),
    )
