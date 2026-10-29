import requests


class BinanceConnector:


    BASE_URL = "https://api.binance.com"


    def get_price(
        self,
        symbol
    ):

        url = (
            f"{self.BASE_URL}"
            f"/api/v3/ticker/price"
            f"?symbol={symbol}"
        )


        response = requests.get(
            url
        )


        data = response.json()


        return {

            "exchange": "Binance",

            "symbol":
            symbol,

            "price":
            float(data["price"])

        }



binance = BinanceConnector()
