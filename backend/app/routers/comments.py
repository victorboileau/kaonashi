from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.db.models import Comment
from app.schemas.comment import CommentCreate, CommentRead
from app.core.security import get_current_user

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("", response_model=CommentRead)
def create_comment(
    data: CommentCreate,
    session: Session = Depends(get_session),
    user = Depends(get_current_user)
):
    comment = Comment(
        content=data.content,
        rating=data.rating,
        recipe_id=data.recipe_id,
        user_id=user.id
    )
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment

@router.get("/recipe/{recipe_id}", response_model=list[CommentRead])
def get_comments_for_recipe(
    recipe_id: int,
    session: Session = Depends(get_session)
):
    return session.exec(
        select(Comment).where(Comment.recipe_id == recipe_id)
    ).all()
