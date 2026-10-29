import os



class BinanceConnector:



    def __init__(self):

        self.api_key = os.getenv(
            "BINANCE_API_KEY"
        )

        self.secret = os.getenv(
            "BINANCE_SECRET"
        )



    def price(
        self,
        symbol
    ):


        return {

            "exchange":
            "Binance",

            "symbol":
            symbol,

            "price":
            "market_price"

        }



    def balance(self):


        return {

            "exchange":
            "Binance",

            "balance":
            0

        }



    def order(
        self,
        side,
        symbol,
        amount
    ):


        return {


            "exchange":
            "Binance",

            "side":
            side,

            "symbol":
            symbol,

            "amount":
            amount,

            "status":
            "prepared"

        }



binance = BinanceConnector()
