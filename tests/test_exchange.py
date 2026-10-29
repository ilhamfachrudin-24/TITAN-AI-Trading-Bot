from app.exchange.manager import exchange_manager




def test_exchange():


    result = exchange_manager.market_price(

        "binance",

        "BTCUSDT"

    )


    assert result["exchange"] == "Binance"
