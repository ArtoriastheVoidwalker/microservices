import enum

from sqlalchemy import Column, Integer, Float, DateTime, Enum, String
from sqlalchemy.sql.sqltypes import Float
from app.db.base_class import Base
from datetime import datetime as dt


class DocEnum(enum.Enum):
    def __new__(cls, value, doc=None):
        self = object.__new__(cls)
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self


class EventState(DocEnum):
    NEW = 'NEW'
    FINISHED_WIN = 'FINISHED_WIN'
    FINISHED_LOSE = 'FINISHED_LOSE'


class Bet(Base):

    id = Column(Integer, primary_key=True, index=True)
    # date = Column(DateTime, nullable=False, default=dt.now)
    event_id = Column(String, nullable=False)
    coefficient = Column(Float, nullable=False)
    sum_bet = Column(Float, nullable=False)
    deadline = Column(Integer, nullable=False)
    state = Column(Enum(EventState), nullable=True)
