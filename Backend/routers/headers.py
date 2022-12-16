from fastapi import APIRouter


router = APIRouter(
    prefix="/headers",
    tags=["Headers"],
)


headline_hero = {
    "titre" : "Healthy eating is important part of lifestyle", 
    "subtitle" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque congue arcu"
}

image_boxes = [
    {
        "image" : "https://technext.github.io/restoran/img/hero.png",
        "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque congue arcu"
    },
    {
        "image" : "https://technext.github.io/restoran/img/hero.png",
        "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Neque congue arcu"
    }
]

    
@router.get("/get_headline_hero", summary="Récupération du titre de la page d'accueil")
def get_headline_hero():
    return headline_hero


@router.get("/get_image_boxes", summary="Récupération des cadres d'images")
def get_image_boxes():
    return image_boxes