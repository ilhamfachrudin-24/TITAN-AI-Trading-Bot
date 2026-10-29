import asyncio


from app.monitoring.logger import log_system



class TitanWorker:


    def __init__(self):

        self.running = False



    async def start(self):


        self.running = True


        log_system(

            "Worker started"

        )


        while self.running:


            await asyncio.sleep(
                10
            )


            log_system(

                "Worker heartbeat"

            )



    def stop(self):

        self.running = False



worker = TitanWorker()
