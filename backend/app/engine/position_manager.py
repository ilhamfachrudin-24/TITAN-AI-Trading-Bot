class PositionManager:



    def calculate_targets(
        self,
        entry,
        risk
    ):


        stop_loss = entry - risk


        take_profit_1 = (

            entry +

            risk * 3

        )


        take_profit_2 = (

            entry +

            risk * 5

        )


        take_profit_3 = (

            entry +

            risk * 8

        )


        return {

            "stop_loss":
            stop_loss,


            "tp1":
            take_profit_1,


            "tp2":
            take_profit_2,


            "tp3":
            take_profit_3

        }



    def trailing_stop(
        self,
        current_price,
        percentage=2
    ):


        return (

            current_price *

            (1 - percentage / 100)

        )



position_manager = PositionManager()
