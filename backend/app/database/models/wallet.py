from sqlalchemy import Column, Integer, String, Float, DateTime

from datetime import datetime


from app.database.postgres import Base




class WalletHistory(Base):


    __tablename__ = "wallet_history"



    id = Column(

        Integer,

        primary_key=True

    )


    wallet = Column(

        String

    )


    chain = Column(

        String

    )


    balance = Column(

        Float

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )
