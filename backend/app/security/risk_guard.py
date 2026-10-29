class RiskGuard:


    def __init__(self):

        self.max_daily_loss = 5

        self.max_position = 20



    def check_position_size(
        self,
        size,
        balance
    ):


        percentage = (

            size /

            balance

        ) * 100



        if percentage > self.max_position:

            return {

                "allowed":
                False,

                "reason":
                "Position terlalu besar"

            }



        return {

            "allowed":
            True,

            "reason":
            "Risk sesuai"

        }



    def check_daily_loss(
        self,
        loss_percentage
    ):


        if loss_percentage >= self.max_daily_loss:

            return {

                "allowed":
                False,

                "reason":
                "Daily loss limit tercapai"

            }



        return {

            "allowed":
            True

        }



risk_guard = RiskGuard()
