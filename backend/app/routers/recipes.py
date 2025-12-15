from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.db.models import Recipe, RecipeCategory
from app.schemas.recipe import RecipeCreate, RecipeRead

router = APIRouter(prefix="/recipes", tags=["recipes"])

@router.get("", response_model=list[RecipeRead])
def get_recipes(session: Session = Depends(get_session)):
    return session.exec(select(Recipe)).all()

@router.get("/{recipe_id}", response_model=RecipeRead)
def get_recipe(recipe_id: int, session: Session = Depends(get_session)):
    recipe = session.get(Recipe, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("", response_model=RecipeRead)
def create_recipe(
    data: RecipeCreate,
    session: Session = Depends(get_session),
    user_id: int = 1  # temporaire (auth plus tard)
):
    recipe = Recipe(
        **data.model_dump(exclude={"category_ids"}),
        author_id=user_id
    )
    session.add(recipe)
    session.commit()
    session.refresh(recipe)

    for category_id in data.category_ids:
        session.add(
            RecipeCategory(
                recipe_id=recipe.id,
                category_id=category_id
            )
        )

    session.commit()
    return recipe
