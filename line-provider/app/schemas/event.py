import decimal
import enum

from typing import Optional
from pydantic import BaseModel


class EventState(enum.Enum):
    NEW = 'NEW'
    FINISHED_WIN = 'FINISHED_WIN'
    FINISHED_LOSE = 'FINISHED_LOSE'


class Event(BaseModel):
    event_id: str
    coefficient: Optional[decimal.Decimal] = None
    deadline: Optional[int] = None
    state: Optional[EventState] = None

    class Config:
        use_enum_values = True


class EventUpdate(BaseModel):
    coefficient: Optional[decimal.Decimal] = None
    deadline: Optional[int] = None
    state: Optional[EventState] = None

    class Config:
        use_enum_values = True