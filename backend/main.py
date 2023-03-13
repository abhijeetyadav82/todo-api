from typing import Union
from apis.type import get_type, get_type_by_name
import uvicorn
from fastapi import Depends, FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.models import Type
from request_body.taskbody import TaskBody
from utils.database import create_table, get_db
from sqlalchemy.orm import Session
from apis.type import get_type
from apis.task import create_task, delete_task_by_id,\
     get_filtered_tasks, get_task_by_id,\
         get_task_count, update_task_by_id



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def show_status(status_code = 200):
    """
        Show the server status. Used to check if server is running.

        ### Return 
        Json object

        **Output Example**
        ```
         {
            "status": "Success",
            "Message": "Service is running"
        }
        ```
    """
    return {"status": "Success",
        "Message": "Service is running"}


@app.get("/type/{type_id}")
def get_type_func(type_id: int,
             db: Session = Depends(get_db)):
    type = get_type(db,type_id)
    if not type:
        raise HTTPException(status_code=404, detail="Type not found")
    return {"id": type.id, "name": type.name}



@app.post("/task/create")
def create_task_func(taskbody : TaskBody,
                     db: Session = Depends(get_db)):
    """
        Create Task

        ### Parameters
        
        - **name**: Str
        - **description**: Str
        - **type**: Str

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    res = create_task(db,taskbody)
    if not res:
        raise HTTPException(status_code=400,detail="Error")

    return {
        "success":True,
        "id": res,
    }

@app.get("/task/getAll")
def get_all_tasks_func(search:Union[str, None] = None,
                        type:Union[str, None] = None,
                        sort:Union[str,None] = None,
                        order:Union[str,None] = "asc",
                        db: Session = Depends(get_db)):
    """
        Get All Tasks

        ### Parameters
        - **filter**: Str   
        - **sort**: Str
        - **order**: Str

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    type_id = None
    type_name = type
    if type_name:
        type = get_type_by_name(db,type)
        if not type:
            raise HTTPException(status_code=400,detail="Invalid Type Name. Please pick from To-Do, In-Progress or Done")
        type_id = type.id
    res = get_filtered_tasks(db,search,type_id,sort,order)
    if not res:
        raise HTTPException(status_code=400,detail="No Tasks Found")

    return {
        "success":True,
        "data": res,
    }


@app.get("/task/get/{task_id}")
def get_task_func(task_id : str,
                db: Session = Depends(get_db)):
    """
        Get All Tasks

        ### Parameters
        - **id**: Str

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    res = get_task_by_id(db,task_id)
    if not res:
        raise HTTPException(status_code=400,detail="Task not found")

    return {
        "success":True,
        "data": res,
    }

@app.post("/task/update/{task_id}")
def update_task_func(task_id : str,
                    taskbody : TaskBody,
                    db: Session = Depends(get_db)):
    """
        Get All Tasks

        ### Parameters
        - **name**: Str
        - **description**: Str
        - **type**: Str
        
        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    res = update_task_by_id(db,task_id,taskbody)
    if not res:
        raise HTTPException(status_code=400,detail="No Task Found")

    return {
        "success":True
    }

@app.delete("/task/delete/{task_id}")
def get_task_func(task_id : str,
                db: Session = Depends(get_db)):
    """
        Get All Tasks

        ### Parameters
        - **id**: Str

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    res = delete_task_by_id(db,task_id)
    if not res:
        raise HTTPException(status_code=400,detail="Task not found")

    return {
        "success":True
            }

@app.get("/task/count")
def get_task_count_func(db: Session = Depends(get_db)):
    """
        Get All Tasks

        ### Parameters

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    res = get_task_count(db)
    if not res:
        raise HTTPException(status_code=400,detail="No Task Found")
    return {
        "success":True,
        "count": res,
    }

@app.post("/types/populate")
def create_type_func(db: Session = Depends(get_db)):
    """
        Create all types

        ### Parameters

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    res = db.query(Type)
    if not res:
        type1,type2,type3 = Type(name="To-Do"),Type(name="In-Progress"),Type(name="Done")
        db.add(type1)
        db.add(type2)
        db.add(type3)
        db.commit()
    return {
        "success":True,
    }

@app.post("/tables")
def create_table_func(db: Session = Depends(get_db)):
    """
        Create all types

        ### Parameters

        ### Return 
        Json object
        
        **Output Example**
        ```
        {
        "success": true
        }
        ```
    """
    create_table()
    db.commit()
    return {
        "success":True,
    }


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
