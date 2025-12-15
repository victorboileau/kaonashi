from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.db.models import Favorite
from app.schemas.favorite import FavoriteRead
from app.core.security import get_current_user

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/{recipe_id}", response_model=FavoriteRead)
def add_favorite(
    recipe_id: int,
    session: Session = Depends(get_session),
    user = Depends(get_current_user)
):
    existing = session.exec(
        select(Favorite)
        .where(Favorite.user_id == user.id)
        .where(Favorite.recipe_id == recipe_id)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already in favorites")

    favorite = Favorite(user_id=user.id, recipe_id=recipe_id)
    session.add(favorite)
    session.commit()
    session.refresh(favorite)
    return favorite

@router.delete("/{recipe_id}")
def remove_favorite(
    recipe_id: int,
    session: Session = Depends(get_session),
    user = Depends(get_current_user)
):
    favorite = session.exec(
        select(Favorite)
        .where(Favorite.user_id == user.id)
        .where(Favorite.recipe_id == recipe_id)
    ).first()

    if not favorite:
        raise HTTPException(status_code=404, detail="Favorite not found")

    session.delete(favorite)
    session.commit()
    return {"status": "deleted"}
