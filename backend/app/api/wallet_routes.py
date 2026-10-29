from fastapi import APIRouter

from app.wallet.wallet_manager import wallet_manager



router = APIRouter(

    prefix="/wallet",

    tags=["Wallet"]

)



@router.post("/connect")

def connect_wallet(data: dict):


    return wallet_manager.connect_wallet(

        data["type"],

        data["address"],

        data.get("network")

    )



@router.post("/analyze")

def analyze_wallet(data: dict):


    return wallet_manager.analyze_wallet(

        data

    )
