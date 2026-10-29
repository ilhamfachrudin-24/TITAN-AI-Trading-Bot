from app.exchange.binance import binance

from app.exchange.bybit import bybit

from app.exchange.okx import okx




class ExchangeManager:



    def __init__(self):

        self.exchanges = {


            "binance":

            binance,


            "bybit":

            bybit,


            "okx":

            okx

        }



    def get_exchange(
        self,
        name
    ):


        return self.exchanges.get(

            name.lower()

        )



    def market_price(
        self,
        exchange,
        symbol
    ):


        connector = self.get_exchange(

            exchange

        )


        return connector.price(

            symbol

        )



    def create_order(
        self,
        exchange,
        side,
        symbol,
        amount
    ):


        connector = self.get_exchange(

            exchange

        )


        return connector.order(

            side,

            symbol,

            amount

        )



exchange_manager = ExchangeManager()
