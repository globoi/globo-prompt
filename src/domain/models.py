from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ContentType(str, Enum):
    NOVEL = "novel"
    VIDEO = "video"


@dataclass
class News:
    id: int
    title: str
    info: str
    author: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Content:
    id: int
    name: str
    description: str
    type: ContentType
    url: str