from fastapi import APIRouter


from app.autotrade.trader import titan_trader

from app.autotrade.scheduler import scheduler



router = APIRouter(

    prefix="/autotrade",

    tags=["Auto Trading"]

)



@router.post("/analyze")

def analyze_trade(data: dict):


    return titan_trader.analyze_and_trade(

        data

    )



@router.post("/start")

def start_bot():


    return scheduler.start()



@router.post("/stop")

def stop_bot():


    return scheduler.stop()



@router.get("/status")

def bot_status():


    return scheduler.status()
