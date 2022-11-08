from fastapi import APIRouter

router = APIRouter()

users = []


@router.get("/")
async def index():
    return {"users": users}
