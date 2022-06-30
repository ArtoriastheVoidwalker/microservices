import decimal
from datetime import date, time

from app.models.bet import EventState
from typing import Optional, List
from pydantic import BaseModel


class Event(BaseModel):
    event_id: str
    state: EventState

    class Config:
        use_enum_values = True


class BetCreate(BaseModel):
    event_id: str
    sum_bet: float
    coefficient: float
    deadline: int
    state: EventState

    class Config:
        use_enum_values = True


class BetInDBBase(Event):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Bet(BetInDBBase):

    class Config:
        use_enum_values = True


class Bets(BaseModel):
    bets: List[Bet] = None
    amount: Optional[int]
