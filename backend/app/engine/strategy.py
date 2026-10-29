class TradingStrategy:


    def analyze(
        self,
        ai_signal,
        market_data
    ):

        decision = ai_signal.get(
            "decision",
            "NO TRADE"
        )


        confidence = ai_signal.get(
            "confidence",
            0
        )


        if confidence < 90:

            return {

                "action": "NO TRADE",

                "reason":
                "Confidence terlalu rendah"

            }


        if decision == "LONG":

            return {

                "action": "LONG",

                "reason":
                "AI consensus LONG"

            }


        if decision == "SHORT":

            return {

                "action": "SHORT",

                "reason":
                "AI consensus SHORT"

            }


        return {

            "action": "NO TRADE",

            "reason":
            "Tidak ada setup valid"

        }



strategy = TradingStrategy()
