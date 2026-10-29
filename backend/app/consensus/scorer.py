class ConsensusScorer:



    def calculate(
        self,
        votes
    ):


        total = sum(

            votes.values()

        )



        if total == 0:

            return {

                "confidence":

                0

            }



        winner = max(

            votes,

            key=votes.get

        )



        confidence = (

            votes[winner]

            /

            total

        ) * 100



        return {


            "decision":

            winner,


            "confidence":

            round(

                confidence,

                2

            )

        }



scorer = ConsensusScorer()
