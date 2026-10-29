import requests


class OKXConnector:


    BASE_URL = (
        "https://www.okx.com"
    )


    def get_price(
        self,
        symbol
    ):


        url = (

            f"{self.BASE_URL}"
            "/api/v5/market/ticker"
            f"?instId={symbol}"

        )


        response = requests.get(
            url
        )


        data = response.json()


        price = (

            data
            ["data"]
            [0]
            ["last"]

        )


        return {

            "exchange":
            "OKX",

            "symbol":
            symbol,

            "price":
            float(price)

        }



okx = OKXConnector()
