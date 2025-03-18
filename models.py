from sqlalchemy import Column, Integer, String
from database import Base

# 🔹 User 모델 정의
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    # password = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
