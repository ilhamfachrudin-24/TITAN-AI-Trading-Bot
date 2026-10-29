from fastapi import APIRouter

from app.connectors.binance import binance
from app.connectors.bybit import bybit
from app.connectors.okx import okx



router = APIRouter(

    prefix="/market",

    tags=["Market"]

)



@router.get("/{symbol}")

def get_market(symbol: str):


    return {


        "binance":

        binance.get_price(
            symbol
        ),


        "bybit":

        bybit.get_price(
            symbol
        ),


        "okx":

        okx.get_price(
            symbol
        )


    }
