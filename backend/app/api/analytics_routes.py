from fastapi import APIRouter


router = APIRouter(

    prefix="/analytics",

    tags=["Analytics"]

)



@router.get("/performance")

def performance():


    return {


        "total_trade":

        0,


        "win_rate":

        0,


        "profit":

        0,


        "loss":

        0,


        "long_trade":

        0,


        "short_trade":

        0,


        "ai_accuracy":

        0

    }
