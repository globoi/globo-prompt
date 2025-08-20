from fastapi import APIRouter

from src.core.database import db_manager

router = APIRouter()


@router.get("/health")
async def health_check():
    try:
        if db_manager.is_healthy():
            return {"status": "healthy", "database": "connected"}
        else:
            return {"status": "unhealthy", "database": "disconnected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "error", "error": str(e)}