from fastapi import APIRouter, Depends, HTTPException, Request, status, Response
# from dependencies import get_token_header


router = APIRouter(
    prefix="/headers",
    tags=["Headers"],
    # dependencies=[Depends(get_token_header)]
)
