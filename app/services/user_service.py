from bson import ObjectId
from app.db.database import db
from app.schemas.user_schema import UserCreate

def create_user(user: UserCreate):
    user_dict = user.dict()
    result = db.users.insert_one(user_dict)
    return str(result.inserted_id)

def get_users():
    users = []
    for user in db.users.find():
        users.append({
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]
        })
    return users
