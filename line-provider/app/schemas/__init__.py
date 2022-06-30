from pydantic import BaseModel
from typing import Optional

from .event import Event, EventState, EventUpdate

class DefaultResponseSchema(BaseModel):

    status_code: Optional[int] = 200
    success: Optional[bool] = True
