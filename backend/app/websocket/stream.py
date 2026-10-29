import asyncio


from app.websocket.manager import manager



async def market_stream():


    while True:


        data = {


            "type":
            "market_update",


            "BTC":

            {

                "price":
                "streaming"

            },


            "AI_SIGNAL":

            "WAITING"


        }



        await manager.broadcast(

            data

        )


        await asyncio.sleep(
            5
        )
