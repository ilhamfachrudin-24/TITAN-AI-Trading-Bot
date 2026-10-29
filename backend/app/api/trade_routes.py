from fastapi import APIRouter


from app.engine.strategy import strategy
from app.engine.execution import execution



router = APIRouter(

    prefix="/trade",

    tags=["Trading"]

)



@router.post("/signal")

def trade_signal(data: dict):


    return strategy.analyze(

        data["ai_signal"],

        data["market"]

    )




@router.post("/execute")

def execute_trade(data: dict):


    return execution.open_trade(

        data["symbol"],

        data["action"],

        data["amount"],

        data["entry"],

        data["stop_loss"],

        data["take_profit"]

    )
