import requests


class BirdeyeConnector:


    BASE_URL = (
        "https://public-api.birdeye.so"
    )


    def get_token(
        self,
        address
    ):


        headers = {

            "X-API-KEY":
            "YOUR_BIRDEYE_KEY"

        }


        url = (

            f"{self.BASE_URL}"
            f"/defi/token_overview"
            f"?address={address}"

        )


        response = requests.get(

            url,

            headers=headers

        )


        return response.json()



birdeye = BirdeyeConnector()
