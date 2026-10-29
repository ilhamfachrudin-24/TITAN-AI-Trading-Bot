import requests


class BybitConnector:


    BASE_URL = (
        "https://api.bybit.com"
    )


    def get_price(
        self,
        symbol
    ):


        url = (

            f"{self.BASE_URL}"
            "/v5/market/tickers"
            f"?category=spot&symbol={symbol}"

        )


        response = requests.get(
            url
        )


        data = response.json()


        price = (

            data
            ["result"]
            ["list"]
            [0]
            ["lastPrice"]

        )


        return {

            "exchange":
            "Bybit",

            "symbol":
            symbol,

            "price":
            float(price)

        }



bybit = BybitConnector()
