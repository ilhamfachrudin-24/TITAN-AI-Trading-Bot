from app.wallet.phantom import phantom
from app.wallet.trust_wallet import trust_wallet
from app.wallet.bitget_wallet import bitget_wallet



class WalletManager:



    def connect_wallet(
        self,
        wallet_type,
        address,
        network=None
    ):


        if wallet_type == "phantom":

            return phantom.connect(
                address
            )


        if wallet_type == "trust":

            return trust_wallet.connect(
                address,
                network
            )


        if wallet_type == "bitget":

            return bitget_wallet.connect(
                address,
                network
            )


        return {

            "status":
            "unsupported wallet"

        }



    def analyze_wallet(
        self,
        wallet_data
    ):


        return {

            "wallet_score":
            0,


            "risk":
            "UNKNOWN",


            "smart_money":
            False

        }



wallet_manager = WalletManager()
