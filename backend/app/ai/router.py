from app.ai.openai import analyze_openai
from app.ai.grok import analyze_grok
from app.ai.claude import analyze_claude
from app.ai.gemini import analyze_gemini
from app.ai.deepseek import analyze_deepseek
from app.ai.perplexity import analyze_perplexity



AI_MODELS = [

    analyze_openai,
    analyze_grok,
    analyze_claude,
    analyze_gemini,
    analyze_deepseek,
    analyze_perplexity

]



def calculate_consensus(results):

    long_votes = 0
    short_votes = 0
    no_trade = 0


    for result in results:

        decision = result.get(
            "decision",
            "NO TRADE"
        )


        if decision == "LONG":
            long_votes += 1

        elif decision == "SHORT":
            short_votes += 1

        else:
            no_trade += 1



    total = len(results)



    if long_votes >= 5:

        return "LONG"


    if short_votes >= 5:

        return "SHORT"


    return "NO TRADE"



def run_ai_consensus(market_data):

    results = []


    for ai_model in AI_MODELS:

        result = ai_model(
            market_data
        )

        results.append(
            result
        )


    decision = calculate_consensus(
        results
    )


    confidence = (

        sum(
            item["confidence"]
            for item in results
        )

        / len(results)

    )



    return {

        "decision": decision,

        "confidence": round(
            confidence,
            2
        ),

        "models": results

    }
