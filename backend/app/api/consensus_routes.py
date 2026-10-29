from fastapi import APIRouter


from app.consensus.voting import voting

from app.consensus.scorer import scorer

from app.consensus.decision import decision_engine



router = APIRouter(

    prefix="/consensus",

    tags=["AI Consensus"]

)



@router.post("/analyze")

def consensus(data:dict):


    votes = voting.vote(

        data["responses"]

    )


    score = scorer.calculate(

        votes

    )


    final = decision_engine.decide(

        score

    )


    return {


        "votes":

        votes,


        "score":

        score,


        "decision":

        final

    }
