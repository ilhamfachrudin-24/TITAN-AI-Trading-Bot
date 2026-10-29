from app.engine.execution import execution


class AutoExecutor:


    def execute(
        self,
        signal_data
    ):


        if signal_data["action"] == "NO TRADE":

            return {

                "status":
                "SKIPPED",

                "reason":
                "Tidak ada sinyal valid"

            }



        result = execution.open_trade(

            signal_data["symbol"],

            signal_data["action"],

            signal_data["amount"],

            signal_data["entry"],

            signal_data["stop_loss"],

            signal_data["take_profit"]

        )


        return result



executor = AutoExecutor()
