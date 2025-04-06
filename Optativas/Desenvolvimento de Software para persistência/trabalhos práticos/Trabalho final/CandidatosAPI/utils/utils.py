from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException

INVALID_ID_ERROR = "Invalid ID format"

def validate_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail=INVALID_ID_ERROR)