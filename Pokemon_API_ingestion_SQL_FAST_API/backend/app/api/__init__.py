from fastapi import APIRouter

from .routes_pokemon import router as pokemon_router
from .routes_stats import router as stats_router

api_router = APIRouter()
api_router.include_router(pokemon_router)
api_router.include_router(stats_router)
