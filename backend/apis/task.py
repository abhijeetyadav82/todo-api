from database.taskdb import create_task_db,get_task_db,get_filtered_tasks_db,\
    get_task_by_id_db,update_task_by_id_db\
        ,delete_task_by_id_db,get_task_count_db
from request_body.taskbody import TaskBody
from utils.models import Task
import datetime

def create_task(db, task_obj : TaskBody):
    task = Task()
    task.name = task_obj.name
    task.description = task_obj.description
    task.create_date = datetime.datetime.now()
    task.modify_date = datetime.datetime.now()
    task.type_id = task_obj.type
    task = create_task_db( db,task)
    return task.id

def get_task(db):
    task = get_task_db(db)
    return task

def get_filtered_tasks(db,search,type_id,sort,order):
    tasks = get_filtered_tasks_db(db,search,type_id,sort,order)
    return tasks

def get_task_by_id(db,id):
    task = get_task_by_id_db(db,id)
    return task

def update_task_by_id(db,id,task_obj : TaskBody):
    task = update_task_by_id_db(db,id,task_obj)
    return task

def delete_task_by_id(db,id):
    task = delete_task_by_id_db(db,id)
    return task

def get_task_count(db):
    counts = get_task_count_db(db)
    return counts