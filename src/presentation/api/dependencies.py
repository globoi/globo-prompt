from fastapi import HTTPException

from src.core.database import db_manager
from src.domain.repositories.news import NewsRepository
from src.domain.repositories.content import ContentRepository


def get_news_repository() -> NewsRepository:
    if not db_manager.is_healthy():
        raise HTTPException(status_code=503, detail="Database not available")
    return NewsRepository()


def get_content_repository() -> ContentRepository:
    if not db_manager.is_healthy():
        raise HTTPException(status_code=503, detail="Database not available")
    return ContentRepository()