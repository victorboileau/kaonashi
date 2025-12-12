from fastapi import FastAPI
from app.routers import health

app = FastAPI(title="Les Recettes de Chihiro API")

app.include_router(health.router)
