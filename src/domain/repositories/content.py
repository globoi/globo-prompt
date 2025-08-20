from typing import List, Optional
from sqlalchemy import text

from src.core.database import db_manager
from ..models import Content, ContentType


class ContentRepository:
    def __init__(self):
        self.db_manager = db_manager
    
    def _row_to_model(self, row) -> Content:
        return Content(
            id=row[0],
            name=row[1],
            description=row[2],
            type=ContentType(row[3]),
            url=row[4]
        )
    
    def find_all(self) -> List[Content]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(text("SELECT * FROM content")).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error fetching all content: {e}")
            return []
    
    def find_by_id(self, id: int) -> Optional[Content]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM content WHERE id = :id"),
                    {"id": id}
                ).fetchone()
                return self._row_to_model(result) if result else None
        except Exception as e:
            print(f"Error fetching content by id: {e}")
            return None
    
    def find_by_type(self, content_type: ContentType) -> List[Content]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM content WHERE type = :content_type"),
                    {"content_type": content_type.value}
                ).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error fetching content by type: {e}")
            return []
    
    def search_by_name(self, search_term: str) -> List[Content]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM content WHERE name ILIKE :search_term"),
                    {"search_term": f"%{search_term}%"}
                ).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error searching content by name: {e}")
            return []
    
    def search_by_description(self, search_term: str) -> List[Content]:
        try:
            with self.db_manager.get_connection() as conn:
                result = conn.execute(
                    text("SELECT * FROM content WHERE description ILIKE :search_term"),
                    {"search_term": f"%{search_term}%"}
                ).fetchall()
                return [self._row_to_model(row) for row in result]
        except Exception as e:
            print(f"Error searching content by description: {e}")
            return []