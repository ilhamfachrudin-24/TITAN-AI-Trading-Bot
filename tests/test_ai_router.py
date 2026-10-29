from app.ai.router import AIRouter



def test_ai_router():


    router = AIRouter()


    result = router.analyze(

        "BTC market analysis"

    )


    assert result is not None
