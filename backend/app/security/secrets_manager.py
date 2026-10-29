import os



class SecretsManager:



    def get(
        self,
        key
    ):


        return os.getenv(

            key

        )



    def validate(
        self,
        keys
    ):


        missing = []



        for key in keys:


            if not self.get(key):

                missing.append(key)



        return {


            "valid":

            len(missing) == 0,


            "missing":

            missing

        }



secrets = SecretsManager()
