from fastapi import APIRouter


from app.memory.ai_memory import ai_memory

from app.memory.trade_memory import trade_memory



router = APIRouter(

    prefix="/memory",

    tags=["Memory"]

)



@router.post("/ai")

def save_ai(data:dict):


    return ai_memory.save_decision(

        data

    )



@router.get("/ai")

def get_ai_history():


    return ai_memory.get_history()



@router.post("/trade")

def save_trade(data:dict):


    return trade_memory.add_trade(

        data

    )



@router.get("/trade")

def get_trade_history():


    return trade_memory.get_trades()
