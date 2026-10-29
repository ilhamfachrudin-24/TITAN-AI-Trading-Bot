from app.consensus.voting import voting
from app.consensus.scorer import scorer



def test_ai_vote():


    responses = [

        {
            "decision":
            "LONG"
        },

        {
            "decision":
            "LONG"
        },

        {
            "decision":
            "SHORT"
        }

    ]



    result = voting.vote(
        responses
    )


    assert result["LONG"] == 2



def test_ai_score():


    score = scorer.calculate({

        "LONG":3,

        "SHORT":1,

        "WAIT":0

    })


    assert score["confidence"] == 75
