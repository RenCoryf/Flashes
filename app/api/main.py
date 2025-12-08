from fastapi import FastAPI, Request

from app.models.api.api_verify_class import ApiVerifyClass

app = FastAPI()


@app.get("/user")
async def get_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if auth_header:
        token = auth_header.split(" ")[1]
        user_id = ApiVerifyClass.verify_token(token)
        if user_id:
            return {"id": user_id}
    return {"error": "Unauthorized"}
