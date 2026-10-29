class APIValidator:



    def validate_keys(
        self,
        keys
    ):


        missing = []


        for name, value in keys.items():


            if not value:

                missing.append(
                    name
                )



        if missing:


            return {

                "valid":
                False,

                "missing":
                missing

            }



        return {


            "valid":
            True

        }



api_validator = APIValidator()
