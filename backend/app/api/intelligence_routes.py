from fastapi import APIRouter


from app.intelligence.token_scanner import token_scanner
from app.intelligence.risk_score import risk_score



router = APIRouter(

    prefix="/intelligence",

    tags=["Intelligence"]

)



@router.post("/scan")

def scan_token(data: dict):


    token = token_scanner.scan(

        data

    )


    return token



@router.post("/risk")

def calculate_risk(data: dict):


    return risk_score.calculate(

        data["token_score"],

        data["whale_score"],

        data["smart_money_score"]

    )
