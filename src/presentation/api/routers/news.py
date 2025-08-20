from fastapi import APIRouter, Depends, HTTPException, Query

from src.domain.repositories.news import NewsRepository
from src.presentation.api.dependencies import get_news_repository

router = APIRouter()


@router.get("/news")
async def get_all_news(
    news_repo: NewsRepository = Depends(get_news_repository)
):
    try:
        news_items = news_repo.find_all()
        return [
            {
                "id": news.id,
                "title": news.title,
                "info": news.info,
                "author": news.author,
                "created_at": news.created_at,
                "updated_at": news.updated_at
            }
            for news in news_items
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news: {str(e)}")


@router.get("/news/search")
async def search_news(
    q: str = Query(..., description="Search term for news title"),
    news_repo: NewsRepository = Depends(get_news_repository)
):
    try:
        news_items = news_repo.search_by_title(q)
        return [
            {
                "id": news.id,
                "title": news.title,
                "info": news.info,
                "author": news.author,
                "created_at": news.created_at,
                "updated_at": news.updated_at
            }
            for news in news_items
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching news: {str(e)}")


@router.get("/news/recent")
async def get_recent_news(
    limit: int = Query(10, description="Number of recent news to fetch"),
    news_repo: NewsRepository = Depends(get_news_repository)
):
    try:
        news_items = news_repo.find_recent(limit)
        return [
            {
                "id": news.id,
                "title": news.title,
                "info": news.info,
                "author": news.author,
                "created_at": news.created_at,
                "updated_at": news.updated_at
            }
            for news in news_items
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recent news: {str(e)}")


@router.get("/news/author/{author}")
async def get_news_by_author(
    author: str,
    news_repo: NewsRepository = Depends(get_news_repository)
):
    try:
        news_items = news_repo.find_by_author(author)
        return [
            {
                "id": news.id,
                "title": news.title,
                "info": news.info,
                "author": news.author,
                "created_at": news.created_at,
                "updated_at": news.updated_at
            }
            for news in news_items
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news by author: {str(e)}")


@router.get("/news/{news_id}")
async def get_news_by_id(
    news_id: int,
    news_repo: NewsRepository = Depends(get_news_repository)
):
    try:
        news = news_repo.find_by_id(news_id)
        if not news:
            raise HTTPException(status_code=404, detail="News not found")
        
        return {
            "id": news.id,
            "title": news.title,
            "info": news.info,
            "author": news.author,
            "created_at": news.created_at,
            "updated_at": news.updated_at
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news: {str(e)}")