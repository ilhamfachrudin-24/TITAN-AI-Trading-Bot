class EmergencyStop:



    def __init__(self):

        self.active = False



    def activate(self):


        self.active = True


        return {

            "status":
            "TRADING STOPPED"

        }



    def deactivate(self):


        self.active = False


        return {

            "status":
            "TRADING ACTIVE"

        }



    def check(self):


        return self.active



emergency_stop = EmergencyStop()
