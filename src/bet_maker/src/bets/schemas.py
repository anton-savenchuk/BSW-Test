from datetime import datetime, timezone

from pydantic import BaseModel, Field, field_serializer


class BetIDSchema(BaseModel):
    bet_id: int


class BetCreateSchema(BaseModel):
    event_id: int
    amount: float

    class Config:
        from_attributes = True


class BetSchema(BetCreateSchema, BetIDSchema):
    created_at: datetime = Field(
        ...,
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )

    @field_serializer("created_at", when_used="json")
    def serialize_format_detetime(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True
