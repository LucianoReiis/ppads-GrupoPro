from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from models.presence import Presence
from config.database import collection_presence
from schema.schemas import list_serial
from .auth import get_current_user
from starlette import status
from bson import ObjectId

router = APIRouter()



# GET Request Method
@router.get("/")
async def get_presences():
    presences = list_serial(collection_presence.find())
    return presences

@router.get("/presence/{student_name}")
async def read_presence(student_name: str):
    student_model = collection_presence.find_one({"student": student_name})
    if student_model is not None:
        student_model["_id"] = str(student_model["_id"])
        return student_model
    else:
        return {"error": "Aluno não encontrado"}

# POST Request Method
@router.post("/")
async def post_presence(presence: Presence, current_user: Annotated[dict, Depends(get_current_user)]):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    
    result = collection_presence.insert_one(dict(presence))
    if result.inserted_id:
        return {"message": "Absence created successfully"}

# PUT Request Method
    


# DELETE Request Method
    
