from fastapi import APIRouter


from app.exchange.manager import exchange_manager



router = APIRouter(

    prefix="/exchange",

    tags=["Exchange"]

)



@router.get("/price")

def price(
    exchange,
    symbol
):


    return exchange_manager.market_price(

        exchange,

        symbol

    )



@router.post("/order")

def order(data:dict):


    return exchange_manager.create_order(

        data["exchange"],

        data["side"],

        data["symbol"],

        data["amount"]

    )
