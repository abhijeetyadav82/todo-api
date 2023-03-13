from utils.models import Type
from sqlalchemy import func

def get_type_db(db,id):
    res = db.query(Type).filter(Type.id == id).first()
    return res 

def get_type_by_name_db(db,name):
    res = db.query(Type).filter(func.lower(Type.name) == func.lower(name)).first()
    return res
