from app.consensus.decision import decision_engine



def test_consensus():

    data = {


        "chatgpt":

        "LONG",


        "claude":

        "LONG",


        "gemini":

        "WAIT"

    }


    result = decision_engine.decide(

        data

    )


    assert "decision" in result
