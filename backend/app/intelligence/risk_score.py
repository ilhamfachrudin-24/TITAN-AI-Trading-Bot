class RiskScore:



    def calculate(
        self,
        token_score,
        whale_score,
        smart_money_score
    ):


        final_score = (

            token_score * 0.4

            +

            whale_score * 0.3

            +

            smart_money_score * 0.3

        )


        return {


            "risk_score":

            round(

                final_score,

                2

            ),


            "rating":

            self.rating(

                final_score

            )

        }



    def rating(
        self,
        score
    ):


        if score >= 80:

            return "LOW RISK"


        if score >= 50:

            return "MEDIUM RISK"


        return "HIGH RISK"



risk_score = RiskScore()
