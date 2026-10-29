class PerformanceAnalyzer:


    def calculate(
        self,
        trades
    ):


        total = len(trades)


        if total == 0:

            return {

                "trades": 0,

                "winrate": 0,

                "profit": 0

            }



        wins = 0

        profit = 0



        for trade in trades:


            pnl = trade.get(
                "pnl",
                0
            )


            profit += pnl


            if pnl > 0:

                wins += 1



        winrate = (

            wins /

            total

        ) * 100



        return {


            "trades":

            total,


            "wins":

            wins,


            "winrate":

            round(
                winrate,
                2
            ),


            "profit":

            round(
                profit,
                2
            )

        }



performance = PerformanceAnalyzer()
