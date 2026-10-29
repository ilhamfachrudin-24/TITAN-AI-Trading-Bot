import hashlib



class Encryption:



    def hash_key(
        self,
        value
    ):


        return hashlib.sha256(

            value.encode()

        ).hexdigest()



    def mask(
        self,
        value
    ):


        if not value:

            return None



        return (

            value[:4]

            +

            "****"

            +

            value[-4:]

        )



encryption = Encryption()
