from sqlalchemy import Column, Integer, String, Float, DateTime, JSON

from datetime import datetime


from app.database.postgres import Base




class AIHistory(Base):


    __tablename__ = "ai_history"



    id = Column(

        Integer,

        primary_key=True

    )


    decision = Column(

        String

    )


    confidence = Column(

        Float

    )


    analysis = Column(

        JSON

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )
