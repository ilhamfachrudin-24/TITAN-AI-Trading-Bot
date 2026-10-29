from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.database.postgres import Base


class Wallet(Base):

    __tablename__ = "wallets"

    id = Column(
        Integer,
        primary_key=True
    )

    address = Column(
        String,
        unique=True
    )

    network = Column(String)

    wallet_type = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class TradePosition(Base):

    __tablename__ = "positions"

    id = Column(
        Integer,
        primary_key=True
    )

    symbol = Column(String)

    side = Column(String)
    # LONG / SHORT

    entry_price = Column(Float)

    stop_loss = Column(Float)

    take_profit = Column(Float)

    leverage = Column(Float)

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class AIAnalysis(Base):

    __tablename__ = "ai_analysis"

    id = Column(
        Integer,
        primary_key=True
    )

    symbol = Column(String)

    decision = Column(String)

    confidence = Column(Float)

    consensus = Column(String)

    analysis = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )



class TradeHistory(Base):

    __tablename__ = "trade_history"

    id = Column(
        Integer,
        primary_key=True
    )

    symbol = Column(String)

    side = Column(String)

    pnl = Column(Float)

    result = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
