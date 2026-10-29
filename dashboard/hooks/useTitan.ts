"use client"


import {
    useEffect,
    useState
} from "react"


import {
    getTitanStatus,
    getBotStatus
}
from "@/lib/api"



export function useTitan(){


    const [
        system,
        setSystem
    ] = useState(null)



    const [
        bot,
        setBot
    ] = useState(null)



    async function refresh(){


        const systemData =
        await getTitanStatus()



        const botData =
        await getBotStatus()



        setSystem(
            systemData
        )


        setBot(
            botData
        )


    }



    useEffect(()=>{


        refresh()



        const timer =
        setInterval(
            refresh,
            10000
        )


        return ()=>clearInterval(
            timer
        )


    },[])



    return {

        system,

        bot,

        refresh

    }

}
