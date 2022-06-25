from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    message: str


@app.get("/", response_model=Message)
def index():
    return Message(message="Hello, world!")


@app.post("/")
def post_accept(body):
    print(body)

    return body


@app.get("/debug-headers")
def print_headers(req: Request):
    return req.headers


class Age(BaseModel):
    age: int


@app.post("/debug-body")
async def print_body(age: Age):
    return age


@app.get("/{name}", response_model=Message)
def greet_person(name: str):
    return Message(message=f"Hello, {name}")
