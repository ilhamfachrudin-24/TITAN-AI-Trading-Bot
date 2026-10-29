class PermissionManager:



    def check_trade_permission(
        self,
        user
    ):


        if user.get(

            "role"

        ) == "admin":


            return {


                "allowed":

                True

            }



        return {


            "allowed":

            False,


            "reason":

            "Permission denied"

        }



permissions = PermissionManager()
