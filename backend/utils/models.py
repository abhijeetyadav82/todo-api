from sqlalchemy import Column, Integer, String
from  utils.database import Base

class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    create_date = Column(String)
    modify_date = Column(String)
    type_id = Column(Integer)
