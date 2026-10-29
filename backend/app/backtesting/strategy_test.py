from app.backtesting.engine import backtester



def run_test():


    sample_trades = [

        {

            "signal":
            "LONG",

            "entry":
            100,

            "exit":
            110

        },


        {

            "signal":
            "SHORT",

            "entry":
            120,

            "exit":
            115

        },


        {

            "signal":
            "LONG",

            "entry":
            130,

            "exit":
            125

        }

    ]



    for trade in sample_trades:


        backtester.execute_trade(

            trade["signal"],

            trade["entry"],

            trade["exit"]

        )



    return backtester.result()
