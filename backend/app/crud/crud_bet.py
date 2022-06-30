from typing import Any
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Bet
from app.schemas import BetCreate, Bets


class CRUDBet(CRUDBase[Bet, BetCreate, Bets]): 

    def create(
        self,
        db: Session,
        *,
        obj_in: BetCreate
    ) -> Bet:

        db_obj = Bet(
            event_id=obj_in.event_id,
            sum_bet=obj_in.sum_bet,
            coefficient=obj_in.coefficient,
            deadline=obj_in.deadline,
            state=obj_in.state
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_bets(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> Any:
        amount = db.query(Bet).count()
        bets = db.query(Bet).offset(skip).limit(limit).all()

        return {'bets': bets, 'amount': amount}

bet = CRUDBet(Bet)
