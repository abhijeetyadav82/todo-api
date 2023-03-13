from utils.constants import DATABASE
from bson import ObjectId
from utils.filter import filter_response_list

def get_bucket_access_by_user_id_db(user_id):
    user_id = ObjectId(user_id)
    db_bucketaccesses = DATABASE["bucketaccesses"]
    res = list(db_bucketaccesses.find({"user":user_id}))
    res = filter_response_list(res)
    return res