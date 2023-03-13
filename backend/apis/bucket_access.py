from database.bucket_accessdb import get_bucket_access_by_user_id_db

def get_bucket_access_by_user_id(user_id):
    bucket_access = get_bucket_access_by_user_id_db(user_id)
    return bucket_access  