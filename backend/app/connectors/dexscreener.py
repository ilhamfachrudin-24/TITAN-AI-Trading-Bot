import requests


class DexscreenerConnector:


    BASE_URL = (
        "https://api.dexscreener.com"
    )


    def get_token_data(
        self,
        chain,
        address
    ):


        url = (

            f"{self.BASE_URL}"
            f"/latest/dex/tokens/"
            f"{address}"

        )


        response = requests.get(
            url
        )


        data = response.json()


        return {

            "source":
            "Dexscreener",

            "chain":
            chain,

            "data":
            data

        }



dexscreener = DexscreenerConnector()
