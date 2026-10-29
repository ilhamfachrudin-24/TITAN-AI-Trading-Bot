class ExecutionEngine:



    def open_trade(
        self,
        symbol,
        action,
        amount,
        entry,
        stop_loss,
        take_profit
    ):


        return {

            "status":
            "EXECUTED",


            "symbol":
            symbol,


            "side":
            action,


            "amount":
            amount,


            "entry":
            entry,


            "stop_loss":
            stop_loss,


            "take_profit":
            take_profit

        }



    def close_trade(
        self,
        position_id
    ):


        return {

            "status":
            "CLOSED",

            "position":
            position_id

        }



execution = ExecutionEngine()
