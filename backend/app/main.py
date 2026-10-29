from fastapi import FastAPI

from app.database.postgres import Base, engine
from app.database import models


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="TITAN AI Trading Bot",
    description="Autonomous AI Crypto Trading Intelligence System",
    version="0.1.0"
)


@app.get("/")
def home():

    return {
        "status": "online",
        "system": "TITAN AI Trading Bot",
        "database": "connected"
    }


@app.get("/health")
def health():

    return {

        "backend": "online",

        "database": "ready",

        "ai_router": "waiting",

        "trading_engine": "waiting"

    }
