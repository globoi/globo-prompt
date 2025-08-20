from typing import Union
from fastapi import FastAPI

from src.presentation.api.routers import health, news, content

app = FastAPI(title="Globo Content API", version="1.0.0")

app.include_router(health.router)
app.include_router(news.router)
app.include_router(content.router)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}