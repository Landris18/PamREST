import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import menus, reservations, headers, articles


tags_metadata = [
    {
        "name": "Root",
        "description": "Racine de l'api",
    },
    {
        "name": "Menus",
        "description": "Toutes les opérations sur les menus",
    },
    {
        "name": "Reservations",
        "description": "Toutes les opérations sur les reservations",
    },
    {
        "name": "Articles",
        "description": "Toutes les opérations relatives sur les articles",
    },
    {
        "name": "Headers",
        "description": "Affichage des contenus sur le header",
    },
]


pam_rest = FastAPI(
    title="PamREST",
    description="API pour une application de restauration",
    version="0.0.1",
    openapi_tags=tags_metadata
)


pam_rest.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

pam_rest.include_router(menus.router)
pam_rest.include_router(reservations.router)
pam_rest.include_router(articles.router)
pam_rest.include_router(headers.router)


@pam_rest.get("/", tags=["Root"], summary="Affichage de message de bienvenu")
async def root():
    return {"message": "Hello from PamREST !"}


if __name__ == '__main__':
    uvicorn.run("main:pam_rest", host='0.0.0.0', port=1600, log_level="info", workers= 10, reload = True)