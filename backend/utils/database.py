from sqlalchemy import create_engine,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String,Table,MetaData

SQLITE_DATABASE_URL = 'sqlite:///todo.db'

engine = create_engine(
    SQLITE_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_table():

    meta = MetaData()

    if not inspect(engine).has_table('type'):
        print("Creating table type")
        type = Table(
        'type', meta, 
        Column('id', Integer, primary_key = True), 
        Column('name', String)
        )
        meta.create_all(engine)

    if not inspect(engine).has_table('tasks'):
        print("Creating table tasks")
        tasks = Table(
        'tasks', meta, 
        Column('id', Integer, primary_key = True), 
        Column('name', String),
        Column('description', String),
        Column('create_date', String),
        Column('modify_date', String),
        Column('type_id', Integer)
        )
        meta.create_all(engine)
