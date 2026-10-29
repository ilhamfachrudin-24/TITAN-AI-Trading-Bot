class SmartMoneyDetector:



    def analyze(
        self,
        wallets
    ):


        smart_wallets = []


        for wallet in wallets:


            if wallet.get(
                "profit_rate",
                0
            ) >= 70:


                smart_wallets.append(
                    wallet
                )



        return {


            "smart_money_detected":

            len(smart_wallets) > 0,


            "wallets":

            smart_wallets,


            "score":

            min(

                len(smart_wallets) * 25,

                100

            )

        }



smart_money = SmartMoneyDetector()
