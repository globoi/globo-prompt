from typing import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from .config import settings


class DatabaseManager:
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self.Base = declarative_base()
        self._initialize()
    
    def _initialize(self):
        try:
            self.engine = create_engine(settings.database_url)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
                print("✅ Database connection successful!")
                
        except SQLAlchemyError as e:
            print(f"❌ Database connection failed: {e}")
            self.engine = None
            self.SessionLocal = None
    
    def get_db_session(self) -> Generator[Session, None, None]:
        if self.SessionLocal is None:
            raise RuntimeError("Database not available")
        
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    @contextmanager
    def get_connection(self):
        if self.engine is None:
            raise RuntimeError("Database engine not available")
        
        with self.engine.connect() as conn:
            yield conn
    
    def is_healthy(self) -> bool:
        try:
            if self.engine:
                with self.engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                return True
            return False
        except Exception:
            return False


db_manager = DatabaseManager()