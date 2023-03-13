from database.typedb import get_type_db, get_type_by_name_db

def get_type(db,id):
    type = get_type_db(db,id)
    return type

def get_type_by_name(db,name):
    type = get_type_by_name_db(db,name)
    return type