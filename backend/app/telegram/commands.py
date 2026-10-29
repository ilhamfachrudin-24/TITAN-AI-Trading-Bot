from app.autotrade.scheduler import scheduler

from app.consensus.decision import decision_engine




class TelegramCommands:



    def status(self):


        return {


            "bot":

            scheduler.status()

        }



    def start(self):


        return scheduler.start()



    def stop(self):


        return scheduler.stop()



    def signal(
        self,
        data
    ):


        return decision_engine.decide(

            data

        )



commands = TelegramCommands()
