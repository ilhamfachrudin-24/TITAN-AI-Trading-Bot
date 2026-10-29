class AIVoting:


    def vote(
        self,
        responses
    ):


        result = {


            "LONG":

            0,


            "SHORT":

            0,


            "WAIT":

            0

        }



        for response in responses:


            decision = response.get(

                "decision",

                "WAIT"

            )


            if decision in result:

                result[decision] += 1



        return result



voting = AIVoting()
