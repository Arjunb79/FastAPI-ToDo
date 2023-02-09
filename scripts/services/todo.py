from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"data": "todo"}
@router.post()

