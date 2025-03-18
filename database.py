from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 URL 설정 (예: PostgreSQL)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:bonnie@localhost:5432/postgres"

# 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 로컬 설정
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 설정
Base = declarative_base()