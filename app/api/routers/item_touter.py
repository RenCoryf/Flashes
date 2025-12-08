from turtle import st

from fastapi import APIRouter, HTTPException, Request, status

router = APIRouter(prefix="/items", tags=["Item"])


@router.post("/bucket/create", status_code=status.HTTP_201_CREATED)
async def create_bucket(request: Request):
    # controller create bucket
    bucket = 228
    if bucket:
        return {"message": "Bucket created successfully"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create bucket"
    )


@router.post("/bucket/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bucket(request: Request):
    # controller delete bucket
    bucket = 228
    if bucket:
        return {"message": "Bucket deleted successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete bucket"
        )


@router.post("/bucket/update", status_code=status.HTTP_200_OK)
async def update_bucket(request: Request):
    # controller update bucket
    bucket = 228
    if bucket:
        return {"message": "Bucket updated successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update bucket"
        )


@router.post("/bucket/list", status_code=status.HTTP_200_OK)
async def list_buckets(request: Request):
    # controller list buckets
    buckets = [228, 229, 230]
    if buckets:
        return {"message": "Buckets listed successfully", "buckets": buckets}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to list buckets"
        )


@router.post("/bucket", status_code=status.HTTP_200_OK)
async def get_bucket(request: Request):
    # controller get bucket details
    bucket = 228
    if bucket:
        return {"message": "Bucket details retrieved successfully", "bucket": bucket}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to retrieve bucket details",
        )
