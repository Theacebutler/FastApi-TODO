from sqlalchemy import Column, String, Integer, DATETIME, Boolean
from datetime import datetime

from .databse import Base



class Task(Base): 
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255), nullable=True)
    created_at = Column(DATETIME, default=datetime.now)
    # TODO add a completed col to te db without breaking it...
    # completed = Column(Boolean, default=False)