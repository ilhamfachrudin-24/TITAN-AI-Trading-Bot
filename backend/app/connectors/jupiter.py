import requests


class JupiterConnector:


    BASE_URL = (
        "https://quote-api.jup.ag"
    )


    def get_quote(
        self,
        input_token,
        output_token,
        amount
    ):


        url = (

            f"{self.BASE_URL}"
            "/v6/quote"

        )


        params = {

            "inputMint":
            input_token,


            "outputMint":
            output_token,


            "amount":
            amount

        }


        response = requests.get(

            url,

            params=params

        )


        return response.json()



jupiter = JupiterConnector()
