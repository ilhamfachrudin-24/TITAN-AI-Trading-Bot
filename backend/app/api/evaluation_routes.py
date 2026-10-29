from fastapi import APIRouter


from app.evaluation.performance import performance

from app.evaluation.evaluator import evaluator

from app.evaluation.feedback import feedback



router = APIRouter(

    prefix="/evaluation",

    tags=["Evaluation"]

)



@router.post("/analyze")

def analyze(data:dict):


    result = performance.calculate(

        data["trades"]

    )



    evaluation = evaluator.evaluate(

        result

    )



    return {


        "performance":

        result,


        "evaluation":

        evaluation,


        "feedback":

        feedback.generate(

            evaluation

        )

    }
