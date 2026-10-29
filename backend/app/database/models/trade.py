from sqlalchemy import Column, Integer, String, Float, DateTime

from datetime import datetime


from app.database.postgres import Base




class Trade(Base):


    __tablename__ = "trades"



    id = Column(

        Integer,

        primary_key=True

    )


    symbol = Column(

        String

    )


    action = Column(

        String

    )


    entry = Column(

        Float

    )


    exit = Column(

        Float,

        nullable=True

    )


    pnl = Column(

        Float,

        default=0

    )


    status = Column(

        String,

        default="OPEN"

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )
