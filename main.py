from fastapi import FastAPI, Query,Path
from pydantic import BaseModel

app = FastAPI()

class Invalidation(BaseModel):
   name : str | None = Query(max_length=5)
   age : int | None

@app.post('/register/{ids}')
async def getName(obj:Invalidation, ids: int = Path(lt=50)):
   return obj, ids