from utils.models import Task
from request_body.taskbody import TaskBody
import datetime

def create_task_db(db,task):
    db.add(task)
    db.commit()
    return task
    
def get_task_db(db):
    res = db.query(Task).all()
    return res

def get_filtered_tasks_db(db,search,type_id,sort,order):
    
    res = db.query(Task)
    
    if type_id:
        res = res.filter(Task.type_id == type_id)
    
    if search:
        search = "%{}%".format(search)
        res = res.filter(Task.name.like(search))
    
    if sort and order == "asc":
        if sort == "create_date":
            res = res.order_by(Task.create_date.asc())
        elif sort == "modify_date":
            res = res.order_by(Task.modify_date.asc())
        elif sort == "name":
            res = res.order_by(Task.name.asc())
    
    if sort and order == "desc":
        if sort == "create_date":
            res = res.order_by(Task.create_date.desc())
        elif sort == "modify_date":
            res = res.order_by(Task.modify_date.desc())
        elif sort == "name":
            res = res.order_by(Task.name.desc())
    
    return res.all()    

def get_task_by_id_db(db,id):
    res = db.query(Task).filter(Task.id == id).first()
    return res

def update_task_by_id_db(db,id,task_obj : TaskBody):
    task = db.query(Task).filter(Task.id == id).update({'name':task_obj.name,
                                                        'description':task_obj.description,
                                                        'modify_date':datetime.datetime.now(),
                                                        'type_id':task_obj.type})
    db.commit()
    return task
    
def delete_task_by_id_db(db,id):
    res = db.query(Task).filter(Task.id == id).delete()
    db.commit()
    return res

def get_task_count_db(db):
    counts = {}
    counts["total"] = db.query(Task).count()
    counts["To-Do"] = db.query(Task).filter(Task.type_id == 1).count()
    counts["In-Progress"] = db.query(Task).filter(Task.type_id == 2).count()
    counts["Done"] = db.query(Task).filter(Task.type_id == 3).count()
    return counts