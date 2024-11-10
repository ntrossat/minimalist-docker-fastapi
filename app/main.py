from fastapi import FastAPI

from app.models.response import MessageResponse
from app.routes import item

app = FastAPI()


@app.get("/")
def read_root() -> MessageResponse:

    return {"message": "Hello World!"}


app.include_router(item.router, prefix="/items", tags=["Items"])
