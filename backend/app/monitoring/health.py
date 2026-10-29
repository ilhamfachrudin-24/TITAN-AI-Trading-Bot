import time



START_TIME = time.time()



class HealthMonitor:


    def status(self):


        uptime = (

            time.time()

            -

            START_TIME

        )


        return {


            "status":

            "healthy",


            "uptime":

            round(
                uptime,
                2
            )

        }



health = HealthMonitor()
