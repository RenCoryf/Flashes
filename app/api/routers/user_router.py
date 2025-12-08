from datetime import datetime
from fastapi import APIRouter, Request

from app.models.dto.users import User_dto
from app.services.api.api_verify_class import ApiVerifyClass

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/")
async def get_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header:
        token = auth_header.split(" ")[1]
        user_id = ApiVerifyClass.verify_token(token)
        if user_id:
            # find user
            user = 228
            return {"user": user}
    return {"error": "Unauthorized"}


@router.post("/registraion")
async def regisrtaion_user(user: User_dto):
    # controler reg user
    user = 228
    if user:
        # controller login user


@router.post("/login")
async def login_user(user: User_dto):
    # controller login user
    user = 228
    if user:
        # controller login user
