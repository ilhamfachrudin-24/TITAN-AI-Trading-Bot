from fastapi import APIRouter


from app.security.secrets_manager import secrets



router = APIRouter(

    prefix="/security",

    tags=["Security"]

)



@router.get("/check")

def security_check():


    return secrets.validate([

        "DATABASE_URL"

    ])
