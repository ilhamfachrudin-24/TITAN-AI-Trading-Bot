from app.consensus.decision import decision_engine



def test_consensus_decision():


    result = decision_engine.decide(

        {

            "decision":
            "LONG",

            "confidence":
            90

        }

    )


    assert result["action"] == "LONG"
