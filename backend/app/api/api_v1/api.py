from fastapi import APIRouter
from .endpoints import (
    bet
)

api_router = APIRouter()

api_router.include_router(bet.router, prefix="/bets", tags=["bets"])
