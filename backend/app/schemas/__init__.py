from pydantic import BaseModel
from typing import Optional

from .bet import (
    Event, Bet, BetCreate, Bets, BetInDBBase
)


class DefaultResponseSchema(BaseModel):

    status_code: Optional[int] = 200
    success: Optional[bool] = True
