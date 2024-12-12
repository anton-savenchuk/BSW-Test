from fastapi import FastAPI

from src.exceptions import EventCannotBeAdded, EventNotFound
from src.schemas import EventCreateSchema, EventSchema
from src.services import EventService


app = FastAPI(
    title="A test service provider of event information.",
    description="This is a very fancy FastAPI project, with auto docs for the API.",
    version="0.1.0",
    contact={
        "name": "Anton Savenchuk",
        "url": "https://github.com/anton-savenchuk",
        "email": "savenchuk.dev@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    root_path="/line-provider",
)


@app.get("/events/")
async def get_events() -> list[EventSchema]:
    "Get all active events"

    return await EventService.get_all_active()


@app.get("/events/{event_id}")
async def get_event(id: int) -> EventSchema:
    "Get an event by ID"

    event = await EventService.get_one(event_id=id)
    if not event:
        raise EventNotFound

    return event


@app.post("/events/create/")
async def create_event(event: EventCreateSchema) -> EventSchema:
    "Create new event"

    new_event = await EventService.create_event(event)
    if not new_event:
        raise EventCannotBeAdded

    return new_event
