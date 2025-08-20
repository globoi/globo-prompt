from typing import List, Optional
from sqlalchemy import text

from src.core.database import db_manager
from ..models import News


class NewsRepository:
    def __init__(self):
        self.db_manager = db_manager
    
    def _row_to_model(self, row) -> News:
        return News(
            id=row[0],
            title=row[1],
            info=row[2],
            author=row[3],
            created_at=row[4],
            updated_at=row[5]
        )
    
    def find_all(self) -> List[News]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(text("SELECT * FROM news ORDER BY created_at DESC")).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error fetching all news: {e}")
            return []
    
    def find_by_id(self, id: int) -> Optional[News]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM news WHERE id = :id"),
                    {"id": id}
                ).fetchone()
                return self._row_to_model(result) if result else None
        except Exception as e:
            print(f"Error fetching news by id: {e}")
            return None
    
    def find_by_author(self, author: str) -> List[News]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM news WHERE author = :author"),
                    {"author": author}
                ).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error fetching news by author: {e}")
            return []
    
    def search_by_title(self, search_term: str) -> List[News]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM news WHERE title ILIKE :search_term"),
                    {"search_term": f"%{search_term}%"}
                ).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error searching news by title: {e}")
            return []
    
    def find_recent(self, limit: int = 10) -> List[News]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM news ORDER BY created_at DESC LIMIT :limit"),
                    {"limit": limit}
                ).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error fetching recent news: {e}")
            return []