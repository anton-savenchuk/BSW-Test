import asyncio

from fastapi import FastAPI

from src.bets.routers import router as router_bets
from src.core.event_consumer import consumer_run
from src.events.routers import router as router_events


async def event_consumer_lifespan(app: FastAPI):
    current_loop = asyncio.get_event_loop()
    current_loop.create_task(consumer_run())

    yield


app = FastAPI(
    title="A test service that accepts bets on events from the user.",
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
    root_path="/bet-maker",
    lifespan=event_consumer_lifespan,
)

app.include_router(router_events)
app.include_router(router_bets)
