from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

post_router = APIRouter()

class Post(BaseModel):
    id: int
    content: str
    media_url: str

mock_posts = [
    {"id": 1, "content": "¡Salud 🍻 desde SocialBrew!", "media_url": "http://localhost:8000/files/sample.jpg"},
    {"id": 2, "content": "Nuevo equipo cervecero disponible 🛠️", "media_url": "http://localhost:8000/files/sample.mp4"}
]

@post_router.get("/posts", response_model=List[Post])
def get_posts():
    return mock_posts