import os



class BybitConnector:



    def __init__(self):

        self.api_key = os.getenv(
            "BYBIT_API_KEY"
        )

        self.secret = os.getenv(
            "BYBIT_SECRET"
        )



    def price(
        self,
        symbol
    ):


        return {


            "exchange":
            "Bybit",

            "symbol":
            symbol,

            "price":
            "market_price"

        }



    def order(
        self,
        side,
        symbol,
        amount
    ):


        return {


            "exchange":
            "Bybit",

            "side":
            side,

            "symbol":
            symbol,

            "amount":
            amount,

            "status":
            "prepared"

        }



bybit = BybitConnector()
