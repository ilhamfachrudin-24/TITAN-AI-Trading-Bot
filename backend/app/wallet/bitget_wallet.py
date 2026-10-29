class BitgetWallet:


    supported_networks = [

        "Solana",

        "Ethereum",

        "BNB Chain"

    ]



    def connect(
        self,
        address,
        network
    ):


        return {

            "wallet":
            "Bitget Wallet",

            "network":
            network,

            "address":
            address,

            "status":
            "connected"

        }



    def portfolio(
        self,
        address
    ):


        return {

            "wallet":
            "Bitget Wallet",

            "address":
            address,

            "portfolio":
            []

        }



bitget_wallet = BitgetWallet()
