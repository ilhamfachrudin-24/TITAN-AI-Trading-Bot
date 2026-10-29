import requests


class HeliusConnector:


    BASE_URL = (
        "https://mainnet.helius-rpc.com"
    )


    def get_wallet_activity(
        self,
        wallet
    ):


        return {

            "wallet":
            wallet,

            "status":
            "waiting_for_api_key"

        }



helius = HeliusConnector()
