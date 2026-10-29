class TokenScanner:



    def scan(
        self,
        token_data
    ):


        liquidity = token_data.get(

            "liquidity",

            0

        )


        volume = token_data.get(

            "volume",

            0

        )



        checks = {



            "liquidity":

            liquidity > 100000,



            "volume":

            volume > 50000,



            "contract":

            True



        }



        score = (

            sum(

                checks.values()

            )

            /

            len(checks)

        ) * 100



        return {


            "token_safe_score":

            round(score,2),


            "checks":

            checks

        }



token_scanner = TokenScanner()
