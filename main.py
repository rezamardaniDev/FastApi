from fastapi import FastAPI, Query,Path, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
  name:  str | None = Query(max_length=10)
  email: str | None = Query(max_length=20)
  password: str | None = Query(min_length=8)


class UserOut(BaseModel):
   name: str
   email: str


@app.post('/register', response_model=UserOut, status_code=status.HTTP_200_OK)
async def getName(user: UserIn):
   if user.name == "admin":
      raise HTTPException(status.HTTP_400_BAD_REQUEST, "user cant set name: admin")
   return user
