class AIFeedback:


    def generate(
        self,
        evaluation
    ):


        return {


            "feedback":

            evaluation["recommendation"],


            "adjustment":

            self.adjust(

                evaluation["winrate"]

            )

        }



    def adjust(
        self,
        winrate
    ):


        if winrate < 60:

            return {

                "risk":

                "decrease",


                "confidence_required":

                95

            }



        return {


            "risk":

            "normal",


            "confidence_required":

            90

        }



feedback = AIFeedback()
