from fastapi import APIRouter

router = APIRouter(
    tags=["Users Routes"]
)

@router.get("/")
def get_root():
    return {"message": "Hello World"}