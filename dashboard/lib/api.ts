const API_URL =
process.env.NEXT_PUBLIC_API_URL ||
"http://localhost:8000"



export async function getTitanStatus(){

    const response =
    await fetch(
        `${API_URL}/`
    )


    return response.json()

}



export async function getBotStatus(){

    const response =
    await fetch(
        `${API_URL}/autotrade/status`
    )


    return response.json()

}



export async function analyzeMarket(
    data:any
){

    const response =
    await fetch(
        `${API_URL}/autotrade/analyze`,
        {

            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:
            JSON.stringify(data)

        }
    )


    return response.json()

}
