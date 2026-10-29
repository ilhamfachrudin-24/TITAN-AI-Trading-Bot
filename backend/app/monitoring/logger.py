import logging


logging.basicConfig(

    level=logging.INFO,

    format=
    "%(asctime)s | %(levelname)s | %(message)s"

)



logger = logging.getLogger(
    "TITAN_AI"
)



def log_trade(message):

    logger.info(

        f"TRADE | {message}"

    )



def log_system(message):

    logger.info(

        f"SYSTEM | {message}"

    )
