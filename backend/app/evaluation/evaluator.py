class AIEvaluator:



    def evaluate(
        self,
        performance_data
    ):


        winrate = performance_data.get(

            "winrate",

            0

        )



        if winrate >= 80:


            status = "EXCELLENT"



        elif winrate >= 60:


            status = "GOOD"



        else:


            status = "NEEDS_IMPROVEMENT"



        return {


            "ai_status":

            status,


            "winrate":

            winrate,


            "recommendation":

            self.recommend(

                winrate

            )

        }



    def recommend(
        self,
        winrate
    ):


        if winrate < 60:

            return (

                "Review strategy "
                "dan kurangi entry"

            )


        return (

            "Strategy berjalan baik"

        )



evaluator = AIEvaluator()
