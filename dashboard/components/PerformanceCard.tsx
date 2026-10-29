"use client"


import {
    useEffect,
    useState
}
from "react"


import {
    getPerformance
}
from "@/lib/analytics"



export default function PerformanceCard(){


const [
data,
setData
]=useState<any>(null)



useEffect(()=>{


getPerformance()

.then(setData)


},[])



return (

<div className="
border
rounded-xl
p-5
">


<h2 className="
text-xl
font-bold
">

📊 Performance

</h2>


{
data &&

<div className="
mt-4
space-y-2
">


<p>
Total Trade:
{data.total_trade}
</p>


<p>
Win Rate:
{data.win_rate}%
</p>


<p>
Profit:
${data.profit}
</p>


<p>
AI Accuracy:
{data.ai_accuracy}%
</p>


</div>

}


</div>

)

}
