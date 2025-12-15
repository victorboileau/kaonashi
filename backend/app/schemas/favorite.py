from pydantic import BaseModel

class FavoriteRead(BaseModel):
    id: int
    user_id: int
    recipe_id: int

    class Config:
        from_attributes = True
