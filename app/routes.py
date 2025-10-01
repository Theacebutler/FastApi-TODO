from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from typing import Any
from sqlalchemy import Column, String, Integer, DATETIME
from datetime import datetime

from .databse import Base
from . import models as m
from .schemas import Task, ResponseTask
from .main import app
from .databse import get_db


router = APIRouter(prefix='/tasks')



@router.post('/add', response_model=Task)
async def add_task(body:Task, db:Session = Depends(get_db)):
    # create a task object = craeat a model Object! not a schema obj...
    newTask = m.Task(
        title =body.title,
        description = body.description
        )
    # save and commit the new object to te db
    db.add(newTask)
    db.commit()
    return newTask



@router.get('/tasks/all', response_model=list[ResponseTask])
async def get_all_tasks(db:Session = Depends(get_db)):
    tasks = db.query(m.Task).order_by(m.Task.created_at).all()
    return tasks


@router.delete('/delete/{id}', response_model=dict[str, ResponseTask])
async def delete_test(id:int, db:Session = Depends(get_db)):
    task_to_delete = db.query(m.Task).filter(m.Task.id == id).first()
    db.delete(task_to_delete)
    db.commit()
    return {'deleted task': task_to_delete}