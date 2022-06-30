import time

from fastapi import APIRouter, Path, HTTPException
from app.schemas import Event, EventState, EventUpdate

router = APIRouter()

events: dict[str, Event] = {
    '1': Event(event_id='1', coefficient=1.2, deadline=int(time.time()) + 600, state=EventState.NEW),
    '2': Event(event_id='2', coefficient=1.15, deadline=int(time.time()) + 60, state=EventState.NEW),
    '3': Event(event_id='3', coefficient=1.67, deadline=int(time.time()) + 90, state=EventState.NEW)
}


@router.put('/event')
async def create_event(event: Event):
    if event.event_id not in events:
        events[event.event_id] = event
        raise HTTPException(status_code=200)
        

    for p_name, p_value in event.dict(exclude_unset=True).items():
        setattr(events[event.event_id], p_name, p_value)

    raise HTTPException(status_code=200)
    

@router.patch("/event/{event_id}")
async def update_current_user(
    event_data: EventUpdate,
    event_id: str = Path(default=None),
):
    if event_id in events:
        events[event_id] = Event(event_id=event_id, coefficient=event_data.coefficient,
                              deadline=event_data.deadline, state=event_data.state)
        raise HTTPException(status_code=200)
        
    raise HTTPException(status_code=404, detail='Event not found')


@router.get('/event/{event_id}')
async def get_event(event_id: str = Path(default=None)):
    if event_id in events:

        return events[event_id]
    
    raise HTTPException(status_code=404, detail="Event not found")


@router.get('/events')
async def get_events():
    return list(e for e in events.values() if time.time() < e.deadline)
