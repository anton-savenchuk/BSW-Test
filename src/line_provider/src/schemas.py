from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.models import EventState


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
        ..., description="Deadline datetime for the event"
    )

    class Config:
        from_attributes = True


class EventUpdateSchema(EventIDSchema, BaseModel):
    event_title: Optional[str] = Field(None, description="Updated event name")
    coefficient: Optional[float] = Field(None, description="Updated coefficient to event")
    deadline: Optional[datetime] = Field(None, description="Updated deadline datetime for the event")

    class Config:
        from_attributes = True


class EventSchema(EventStateSchema, EventCreateSchema, EventIDSchema):
    class Config:
        from_attributes = True
