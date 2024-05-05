from fastapi import FastAPI
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int | None


app = FastAPI()


@app.post('/home')
async def root(prs: Person):
    return prs.name
