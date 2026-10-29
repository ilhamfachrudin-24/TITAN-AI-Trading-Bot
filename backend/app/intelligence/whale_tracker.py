class WhaleTracker:



    def analyze_wallet(
        self,
        wallet_activity
    ):


        transactions = (

            wallet_activity.get(
                "transactions",
                []
            )

        )


        large_moves = []


        for tx in transactions:


            if tx.get(
                "value",
                0
            ) > 100000:


                large_moves.append(tx)



        return {


            "whale_activity":

            len(large_moves) > 0,


            "large_transactions":

            large_moves,


            "score":

            min(

                len(large_moves) * 20,

                100

            )

        }



whale_tracker = WhaleTracker()
