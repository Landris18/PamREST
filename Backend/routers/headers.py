from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header


router = APIRouter(
    prefix="/headers",
    tags=["headers"],
    dependencies=[Depends(get_token_header)]
)
