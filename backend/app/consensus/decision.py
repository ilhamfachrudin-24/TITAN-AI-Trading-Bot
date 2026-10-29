class FinalDecision:



    def decide(
        self,
        consensus
    ):


        confidence = consensus.get(

            "confidence",

            0

        )


        decision = consensus.get(

            "decision"

        )



        if confidence < 75:


            return {


                "action":

                "WAIT",


                "reason":

                "Confidence rendah"

            }



        return {


            "action":

            decision,


            "confidence":

            confidence,


            "reason":

            "AI consensus valid"

        }



decision_engine = FinalDecision()
