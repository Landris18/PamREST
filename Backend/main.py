import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import menus, reservations


pam_rest = FastAPI()

pam_rest.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

pam_rest.include_router(menus.router)
pam_rest.include_router(reservations.router)


@pam_rest.get("/")
async def root():
    return {"message": "Hello from PamREST !"}


if __name__ == '__main__':
    uvicorn.run("main:pam_rest", host='0.0.0.0', port=1600, log_level="info", reload = True)
    print("The server is running...")