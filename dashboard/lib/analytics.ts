const API_URL =
process.env.NEXT_PUBLIC_API_URL ||
"http://localhost:8000"



export async function getPerformance(){


    const response =
    await fetch(

        `${API_URL}/analytics/performance`

    )


    return response.json()

}
