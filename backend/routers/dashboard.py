from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary")
def summary():
    return {"message":"Dashboard summary endpoint (demo)"}
