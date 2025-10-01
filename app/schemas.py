from typing import Any
from pydantic import BaseModel, Field
from datetime import datetime


class Task(BaseModel):
    ''' an object to creaet at the post route'''
    title: str
    description: str | None

class ResponseTask(BaseModel):
    '''a response object, adding the id and date created'''
    id: int
    title: str
    description: str | None
    created_at: datetime
    copmleted: bool