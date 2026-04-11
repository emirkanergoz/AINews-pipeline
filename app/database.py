from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# DOĞRU URL: create_all diye bir şey import etmiyoruz, o models kısmında metadata üzerinden çağrılır.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/ainews")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()