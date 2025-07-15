from typing import Union
import os
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

app = FastAPI(title="FastAPI App", version="1.0.0")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fastapi_db")

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        
except SQLAlchemyError as e:
    print(f"❌ Database connection failed: {e}")
    engine = None
    SessionLocal = None
    Base = None

def get_db():
    if SessionLocal is None:
        raise HTTPException(status_code=503, detail="Database not available")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World", "message": "FastAPI com PostgreSQL!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/health")
async def health_check():
    try:
        if engine:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return {"status": "healthy", "database": "connected"}
        else:
            return {"status": "unhealthy", "database": "disconnected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "error", "error": str(e)}
