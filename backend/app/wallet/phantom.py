class PhantomWallet:


    network = "Solana"


    def connect(
        self,
        address
    ):

        return {

            "wallet":
            "Phantom",

            "network":
            self.network,

            "address":
            address,

            "status":
            "connected"

        }



    def get_balance(
        self,
        address
    ):

        return {

            "wallet":
            "Phantom",

            "address":
            address,

            "balance":
            "pending_rpc"

        }



phantom = PhantomWallet()
