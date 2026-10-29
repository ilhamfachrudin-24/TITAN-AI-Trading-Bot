import time


class TradingScheduler:



    def __init__(self):

        self.running = False



    def start(self):

        self.running = True


        return {

            "status":
            "scheduler_started"

        }



    def stop(self):

        self.running = False


        return {

            "status":
            "scheduler_stopped"

        }



    def status(self):

        return {

            "running":
            self.running

        }



scheduler = TradingScheduler()
