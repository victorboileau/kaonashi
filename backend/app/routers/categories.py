from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db.session import get_session
from app.db.models import Category
from app.schemas.category import CategoryRead

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("", response_model=list[CategoryRead])
def get_categories(session: Session = Depends(get_session)):
    return session.exec(select(Category)).all()
