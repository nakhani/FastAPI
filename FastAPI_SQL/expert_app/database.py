from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://uni-admin:92422176@localhost:5432/university_db"
#SQLALCHEMY_DATABASE_URL = "postgresql://root:lYoWgprTDAs31JXb6bfdYJeO@university-db:5432/postgres" # Liara Link

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
