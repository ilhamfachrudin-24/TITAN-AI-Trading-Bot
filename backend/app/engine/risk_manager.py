class RiskManager:


    def calculate_position(
        self,
        balance,
        risk_percent,
        entry_price,
        stop_loss
    ):


        risk_amount = (

            balance *

            risk_percent /

            100

        )


        distance = abs(

            entry_price -

            stop_loss

        )


        if distance == 0:

            return 0


        position_size = (

            risk_amount /

            distance

        )


        return round(
            position_size,
            4
        )



    def validate_trade(
        self,
        risk_reward,
        confidence
    ):


        if confidence < 90:

            return False


        if risk_reward < 3:

            return False


        return True



risk_manager = RiskManager()
