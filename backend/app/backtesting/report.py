class BacktestReport:



    def generate(
        self,
        data
    ):


        return {


            "TITAN AI BACKTEST REPORT": {


                "balance":
                data["ending_balance"],


                "trade_count":
                data["total_trade"],


                "winrate":
                data["winrate"]

            }


        }



report = BacktestReport()
