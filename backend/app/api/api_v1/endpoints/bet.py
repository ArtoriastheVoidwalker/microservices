import json
import requests as r

from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()

@router.get("/events")
async def get_events():
    resp = r.get(settings.EVENT_URL)
    json_resp = json.loads(resp.text)
    return json_resp
    
    
@router.get("/bets", response_model=schemas.Bets)
async def get_bets(
    db: Session = Depends(deps.get_db),
    page: int = 1,
    count: int = 10,
) -> Any:

    skip = (page - 1) * count
    
    bets = crud.bet.get_bets(db, skip=skip, limit=count)

    return bets


@router.post("/bet/{event_id}/{sum_bet}")
async def create(
    *,
    event_id: str,
    sum_bet: float,
    db: Session = Depends(deps.get_db),
) -> Any:
    resp = r.get(settings.EVENT_URL)
    json_resp = json.loads(resp.text)
    for event in json_resp:
        if event['event_id'] == event_id:
            result = crud.bet.create(db, obj_in=schemas.BetCreate(
                event_id=event_id,
                sum_bet=sum_bet,
                coefficient=event['coefficient'],
                deadline=event['deadline'],
                state=event['state']
        ))
            return result

    

    
    