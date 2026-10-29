from fastapi import FastAPI


from app.database.postgres import Base, engine


from app.api import (

    ai_routes,

    market_routes,

    wallet_routes,

    trade_routes,

    backtest_routes,

    security_routes,

    intelligence_routes,

    autotrade_routes

)



Base.metadata.create_all(

    bind=engine

)



app = FastAPI(

    title="TITAN AI Trading Bot",

    version="1.0.0"

)



app.include_router(ai_routes.router)

app.include_router(market_routes.router)

app.include_router(wallet_routes.router)

app.include_router(trade_routes.router)

app.include_router(backtest_routes.router)

app.include_router(security_routes.router)

app.include_router(intelligence_routes.router)

app.include_router(autotrade_routes.router)



@app.get("/")

def home():

    return {

        "system":
        "TITAN AI Trading Bot",

        "status":
        "online",

        "mode":
        "AI Automated Trading Framework"

    }
