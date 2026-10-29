class TradeJournal:



    def create_entry(
        self,
        trade,
        ai_reason
    ):


        return {


            "symbol":

            trade.get(
                "symbol"
            ),


            "action":

            trade.get(
                "action"
            ),


            "entry":

            trade.get(
                "entry"
            ),


            "ai_reason":

            ai_reason,


            "status":

            "OPEN"

        }



    def close_entry(
        self,
        journal,
        result
    ):


        journal["result"] = result

        journal["status"] = "CLOSED"


        return journal



journal = TradeJournal()
