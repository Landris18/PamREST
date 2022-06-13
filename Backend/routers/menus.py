from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_token_header

router = APIRouter(
    prefix="/menus",
    tags=["menus"],
    dependencies=[Depends(get_token_header)]
)