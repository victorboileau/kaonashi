from pydantic import BaseModel
from datetime import datetime

class RecipeBase(BaseModel):
    title: str
    film_series: str
    ingredients: str
    instructions: str

class RecipeCreate(RecipeBase):
    category_ids: list[int]

class RecipeRead(RecipeBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        from_attributes = True
