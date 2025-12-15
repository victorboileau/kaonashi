from fastapi import FastAPI
from app.routers import comments, favorites, recipes, categories, health

app = FastAPI(title="Les Recettes de Chihiro API")

app.include_router(health.router)
app.include_router(recipes.router)
app.include_router(categories.router)
app.include_router(comments.router)
app.include_router(favorites.router)
