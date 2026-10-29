from app.ai.router import run_ai_consensus

from app.engine.strategy import strategy

from app.security.risk_guard import risk_guard

from app.autotrade.executor import executor



class TitanTrader:



    def analyze_and_trade(
        self,
        market_data
    ):


        ai_result = run_ai_consensus(

            market_data

        )



        strategy_result = strategy.analyze(

            ai_result,

            market_data

        )



        if strategy_result["action"] == "NO TRADE":


            return {


                "status":
                "WAITING",


                "analysis":
                strategy_result

            }



        risk = risk_guard.check_position_size(

            market_data["amount"],

            market_data["balance"]

        )



        if not risk["allowed"]:


            return {


                "status":
                "BLOCKED",


                "reason":
                risk["reason"]

            }



        trade = executor.execute({

            **market_data,

            **strategy_result

        })



        return {


            "ai":

            ai_result,


            "trade":

            trade

        }



titan_trader = TitanTrader()
