from fastapi import FastAPI

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
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "database": "pending",
        "ai_router": "pending",
        "trading_engine": "pending"
    }
