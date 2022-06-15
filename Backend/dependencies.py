from fastapi import Header, HTTPException
from os import environ as env
from dotenv import load_dotenv


load_dotenv()


async def get_token_header(jwt_token: str = Header(default="")):
    if jwt_token != env.get("JWT_TOKEN"):
        raise HTTPException(status_code=401, detail="JWT Token header invalid")
