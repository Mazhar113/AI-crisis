from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: dict):
    return {"message":"Login endpoint (demo)"}

@router.post("/register")
def register(data: dict):
    return {"message":"Register endpoint (demo)"}
