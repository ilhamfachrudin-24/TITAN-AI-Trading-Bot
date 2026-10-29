class BacktestEngine:


    def __init__(self):

        self.balance = 10000

        self.trades = []



    def execute_trade(
        self,
        signal,
        entry,
        exit_price
    ):


        if signal == "LONG":

            pnl = (
                exit_price - entry
            )


        elif signal == "SHORT":

            pnl = (
                entry - exit_price
            )


        else:

            pnl = 0



        self.trades.append({

            "signal":
            signal,

            "entry":
            entry,

            "exit":
            exit_price,

            "pnl":
            pnl

        })


        self.balance += pnl


        return pnl



    def result(self):


        total = len(
            self.trades
        )


        wins = len([

            trade

            for trade

            in self.trades

            if trade["pnl"] > 0

        ])



        winrate = 0


        if total > 0:

            winrate = (

                wins /

                total

            ) * 100



        return {


            "starting_balance":
            10000,


            "ending_balance":
            self.balance,


            "total_trade":
            total,


            "winrate":
            round(
                winrate,
                2
            )

        }



backtester = BacktestEngine()
