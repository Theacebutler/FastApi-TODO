from typing import Any

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import models as m
from .databse import get_db
from .schemas import ResponseTask, Task

router = APIRouter(prefix="/tasks")


@router.post("/add", response_model=Task)
async def add_task(body: Task, db: Session = Depends(get_db)):
    # create a task object = craeat a model Object! not a schema obj...
    newTask = m.Task(title=body.title, description=body.description)
    # save and commit the new object to te db
    db.add(newTask)
    db.commit()
    response = jsonable_encoder({"message": f"task {body.title} created!"})
    return JSONResponse(response)


@router.get("/all", response_model=Any)
async def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(m.Task).order_by(m.Task.created_at).all()
    # encode the db query in to JSON
    jsonData = jsonable_encoder(tasks)
    return JSONResponse(content=jsonData)


@router.get("/all/open/", response_model=list[Task])
async def get_open_tasks(db: Session = Depends(get_db)):
    tasks = (
        db.query(m.Task)
        .filter(m.Task.copmleted is False)
        .order_by(m.Task.created_at)
        .all()
    )
    # encode the db query in to JSON
    jsonData = jsonable_encoder(tasks)
    return JSONResponse(content=jsonData)


@router.delete("/delete/{id}", response_model=dict[str, ResponseTask])
async def delete_task(id: int, db: Session = Depends(get_db)):
    task_to_delete = db.query(m.Task).filter(m.Task.id == id).first()
    db.delete(task_to_delete)
    db.commit()
    response = jsonable_encoder({"message": "deleted task"})
    return JSONResponse(response)
