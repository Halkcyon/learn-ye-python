from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    message: str


@app.get("/", response_model=Message)
def index():
    return Message(message="Hello, world!")


@app.get("/{name}", response_model=Message)
def greet_person(name: str):
    return Message(message=f"Hello, {name}")
