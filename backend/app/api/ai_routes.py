from fastapi import APIRouter

from app.ai.router import run_ai_consensus


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)



@router.post("/analyze")
def analyze_market(data: dict):


    result = run_ai_consensus(
        data
    )


    return {

        "system":
        "TITAN AI",

        "result":
        result

    }
