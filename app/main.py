from fastapi import FastAPI

from .databse import create_tables


app = FastAPI()

from . import routes as tasks
app.include_router(tasks.router)


# create the db tables
create_tables()