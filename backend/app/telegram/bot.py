import requests

from app.config import settings



class TelegramMonitor:



    def __init__(self):

        self.token = (
            settings.TELEGRAM_BOT_TOKEN
        )

        self.chat_id = (
            settings.TELEGRAM_CHAT_ID
        )



    def send_message(
        self,
        message
    ):


        if not self.token:

            return {

                "status":
                "telegram_not_configured"

            }



        url = (

            f"https://api.telegram.org/"
            f"bot{self.token}/sendMessage"

        )


        payload = {

            "chat_id":
            self.chat_id,

            "text":
            message

        }


        response = requests.post(

            url,

            json=payload

        )


        return response.json()



    def trade_alert(
        self,
        symbol,
        action,
        price
    ):


        message = f"""

🚀 TITAN AI TRADE ALERT


Symbol:
{symbol}


Action:
{action}


Price:
{price}


System:
AI Consensus Engine


"""


        return self.send_message(
            message
        )



    def risk_alert(
        self,
        message
    ):


        return self.send_message(

            f"""

⚠️ TITAN AI RISK ALERT


{message}


"""

        )



telegram_monitor = TelegramMonitor()
