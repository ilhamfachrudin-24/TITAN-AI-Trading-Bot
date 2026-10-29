from fastapi import APIRouter


from app.monitoring.health import health



router = APIRouter(

    prefix="/health",

    tags=["Monitoring"]

)



@router.get("")

def health_check():


    return health.status()
