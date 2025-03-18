from fastapi import FastAPI
from database import engine
import models
from routers import users  # ✅ users.py를 FastAPI에 등록
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)  # ✅ users.py의 라우터를 FastAPI에 추가