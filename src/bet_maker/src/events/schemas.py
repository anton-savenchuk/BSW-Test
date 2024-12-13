from datetime import datetime, timezone

from pydantic import BaseModel, Field, field_serializer


class EventSchema(BaseModel):
    event_id: int
    event_title: str
    coefficient: float
    deadline: datetime = Field(
        ...,
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )
    state: int

    @field_serializer("deadline", when_used="json")
    def serialize_format_deadline(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True