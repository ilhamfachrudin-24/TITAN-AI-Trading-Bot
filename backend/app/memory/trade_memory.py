class TradeMemory:



    def __init__(self):

        self.trades = []



    def add_trade(
        self,
        trade
    ):


        self.trades.append(

            trade

        )


        return {

            "saved":
            True,

            "total":

            len(self.trades)

        }



    def get_trades(self):


        return self.trades



trade_memory = TradeMemory()
