from app.engine.strategy import strategy



def test_trade_wait():


    result = strategy.analyze(

        {

            "decision":
            "LONG",

            "confidence":
            50

        },

        {}

    )


    assert result["action"] == "NO TRADE"
