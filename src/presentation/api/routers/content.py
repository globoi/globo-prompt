from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query

from src.domain.models import ContentType
from src.domain.repositories.content import ContentRepository
from src.presentation.api.dependencies import get_content_repository

router = APIRouter()


@router.get("/content")
async def get_all_content(
    content_repo: ContentRepository = Depends(get_content_repository)
):
    try:
        content_items = content_repo.find_all()
        return {
            "status": "healthy", 
            "database": "connected", 
            "content": [
                {
                    "id": content.id,
                    "name": content.name,
                    "description": content.description,
                    "type": content.type.value,
                    "url": content.url
                }
                for content in content_items
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching content: {str(e)}")


@router.get("/content/{content_id}")
async def get_content_by_id(
    content_id: int,
    content_repo: ContentRepository = Depends(get_content_repository)
):
    try:
        content = content_repo.find_by_id(content_id)
        if not content:
            raise HTTPException(status_code=404, detail="Content not found")
        
        return {
            "id": content.id,
            "name": content.name,
            "description": content.description,
            "type": content.type.value,
            "url": content.url
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching content: {str(e)}")


@router.get("/content/type/{content_type}")
async def get_content_by_type(
    content_type: ContentType,
    content_repo: ContentRepository = Depends(get_content_repository)
):
    try:
        content_items = content_repo.find_by_type(content_type)
        return [
            {
                "id": content.id,
                "name": content.name,
                "description": content.description,
                "type": content.type.value,
                "url": content.url
            }
            for content in content_items
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching content by type: {str(e)}")


@router.get("/content/search")
async def search_content(
    q: str = Query(..., description="Search term for content name or description"),
    search_in: str = Query("name", description="Search in 'name' or 'description'"),
    content_repo: ContentRepository = Depends(get_content_repository)
):
    try:
        if search_in == "description":
            content_items = content_repo.search_by_description(q)
        else:
            content_items = content_repo.search_by_name(q)
        
        return [
            {
                "id": content.id,
                "name": content.name,
                "description": content.description,
                "type": content.type.value,
                "url": content.url
            }
            for content in content_items
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching content: {str(e)}")