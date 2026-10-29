import os
import requests



class TelegramNotifier:



    def __init__(self):

        self.token = os.getenv(

            "TELEGRAM_TOKEN"

        )

        self.chat_id = os.getenv(

            "TELEGRAM_CHAT_ID"

        )



    def send(
        self,
        message
    ):


        if not self.token or not self.chat_id:

            return {

                "status":
                "telegram_not_configured"

            }



        url = (

            "https://api.telegram.org/bot"

            +

            self.token

            +

            "/sendMessage"

        )



        payload = {


            "chat_id":

            self.chat_id,


            "text":

            message

        }



        requests.post(

            url,

            json=payload

        )



        return {


            "status":

            "sent"

        }



notifier = TelegramNotifier()
