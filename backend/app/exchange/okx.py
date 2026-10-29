import os



class OKXConnector:



    def __init__(self):

        self.api_key = os.getenv(
            "OKX_API_KEY"
        )

        self.secret = os.getenv(
            "OKX_SECRET"
        )



    def price(
        self,
        symbol
    ):


        return {


            "exchange":
            "OKX",

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
            "OKX",

            "side":
            side,

            "symbol":
            symbol,

            "amount":
            amount,

            "status":
            "prepared"

        }



okx = OKXConnector()
