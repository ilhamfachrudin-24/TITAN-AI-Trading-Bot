class AIMemory:


    def __init__(self):

        self.records = []



    def save_decision(
        self,
        analysis
    ):


        self.records.append({

            "type":
            "AI_DECISION",

            "data":
            analysis

        })


        return {

            "status":
            "saved",

            "memory_count":
            len(self.records)

        }



    def get_history(self):


        return self.records



ai_memory = AIMemory()
