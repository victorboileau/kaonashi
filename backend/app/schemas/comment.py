from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str
    rating: float
    recipe_id: int

class CommentRead(BaseModel):
    id: int
    content: str
    rating: float
    user_id: int
    recipe_id: int
    created_at: datetime

    class Config:
        from_attributes = True
