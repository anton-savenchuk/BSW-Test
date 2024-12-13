from fastapi import APIRouter

from src.events.exceptions import EventNotFound
from src.events.schemas import EventSchema
from src.events.services import EventService


router = APIRouter(
    prefix="/events",
    tags=["Events"],
)


@router.get("/")
async def get_events() -> list[EventSchema]:
    "Get all active events"

    return await EventService.get_all_active()


@router.get("/{event_id}")
async def get_event(event_id: int) -> EventSchema:
    "Get an event by ID"

    event = await EventService.get_one(event_id=event_id)
    if not event:
        raise EventNotFound

    return event
