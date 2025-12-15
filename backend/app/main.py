from fastapi import FastAPI
from app.routers import recipes, categories, health

app = FastAPI(title="Les Recettes de Chihiro API")

app.include_router(health.router)
app.include_router(recipes.router)
app.include_router(categories.router)
