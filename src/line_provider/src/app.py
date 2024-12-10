from fastapi import FastAPI


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


@app.get("/")
def hello():
    return {"message": "Hello, World!"}