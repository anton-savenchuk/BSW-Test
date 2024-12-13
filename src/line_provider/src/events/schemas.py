from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from src.core.config import settings
from src.events.models import EventState


class EventIDSchema(BaseModel):
    event_id: int


class EventStateSchema(BaseModel):
    state: EventState = Field(..., description="Event status")

    class Config:
        from_attributes = True


class EventCreateSchema(BaseModel):
    event_title: str = Field(..., description="Event name")
    coefficient: float = Field(..., description="Coefficient to event", ge=0)
    deadline: datetime = Field(
        ...,
        description=f"Deadline datetime for the event, min {settings.TIMEDELTA} minutes before start, format YYYY-MM-DD HH:MM",
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )

    @field_serializer("deadline", when_used="json")
    def serialize_format_deadline(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True


class EventUpdateSchema(EventIDSchema, BaseModel):
    event_title: Optional[str] = Field(None, description="Updated event name")
    coefficient: Optional[float] = Field(
        None, description="Updated coefficient to event"
    )
    deadline: Optional[datetime] = Field(
        None,
        description=f"Updated deadline datetime for the event, min {settings.TIMEDELTA} minutes before start, format YYYY-MM-DD HH:MM",
        example=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
    )

    @field_serializer("deadline", when_used="json")
    def serialize_format_deadline(self, deadline: datetime):
        return deadline.strftime("%Y-%m-%d %H:%M")

    class Config:
        from_attributes = True


class EventSchema(EventStateSchema, EventCreateSchema, EventIDSchema):
    class Config:
        from_attributes = True
