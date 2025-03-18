from database import engine, Base

# 🔹 데이터베이스 테이블 생성
print("📌 데이터베이스 테이블 생성 중...")
Base.metadata.create_all(bind=engine)
print("✅ 테이블 생성 완료!")
