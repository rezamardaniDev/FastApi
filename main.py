from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engin, SessionLocal
import schemas, models


models.Base.metadata.create_all(bind=engin)
app = FastAPI()


def get_db():
   db = SessionLocal()
   try:
        yield db
   finally:
      db.close()


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email==user.email).first()
    if db_user:
        raise HTTPException(status_code=400 , detail="user are exist!")
    user = models.User(email=user.email, username=user.username, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get('/users/{user_id}', response_model=schemas.User)
async def get_user(user_id:int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    return db_user
