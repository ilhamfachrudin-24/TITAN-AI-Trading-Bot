from app.backtesting.engine import BacktestEngine



def test_backtest():


    engine = BacktestEngine()


    pnl = engine.execute_trade(

        "LONG",

        100,

        110

    )


    assert pnl == 10
