from fastapi import APIRouter


from app.telegram.notifier import notifier



router = APIRouter(

    prefix="/telegram",

    tags=["Telegram"]

)



@router.post("/notify")

def notify(data:dict):


    return notifier.send(

        data["message"]

    )
