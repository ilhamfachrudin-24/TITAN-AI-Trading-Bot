import time



class RateLimiter:



    def __init__(self):

        self.requests = {}



    def allow(
        self,
        client,
        limit=10
    ):


        now = time.time()



        if client not in self.requests:


            self.requests[client] = []



        self.requests[client] = [

            x for x in self.requests[client]

            if now - x < 60

        ]



        if len(self.requests[client]) >= limit:


            return False



        self.requests[client].append(

            now

        )


        return True



limiter = RateLimiter()
