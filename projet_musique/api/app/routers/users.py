from fastapi import APIRouter

router = APIRouter(
    tags=['users']
)

fake_db = [{"username": "rick"},
           {"username": "morty"}]


@router.get("/users")
async def read_users():
    """
    Retourne les utilisateurs
    """
    return fake_db
