from fastapi import APIRouter

from app.backtesting.strategy_test import run_test



router = APIRouter(

    prefix="/backtest",

    tags=["Backtest"]

)



@router.get("/run")

def run_backtest():


    return run_test()
