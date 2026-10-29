from fastapi import APIRouter

from app.security.emergency_stop import emergency_stop



router = APIRouter(

    prefix="/security",

    tags=["Security"]

)



@router.post("/stop")

def stop_bot():

    return emergency_stop.activate()



@router.post("/start")

def start_bot():

    return emergency_stop.deactivate()



@router.get("/status")

def status():

    return {


        "trading_stopped":

        emergency_stop.check()

    }
