"use client"


import {
    useEffect,
    useState
}
from "react"


import {
    connectTitanSocket
}
from "@/lib/websocket"



export default function MarketStream(){


const [
data,
setData
]=useState(null)



useEffect(()=>{


const socket =
connectTitanSocket(
    setData
)



return ()=>socket.close()


},[])



return (

<div className="
border
rounded-xl
p-5
">


<h2 className="
font-bold
text-xl
">

📡 Live Market Stream

</h2>


<pre className="mt-4">

{
JSON.stringify(
data,
null,
2
)
}

</pre>


</div>

)


}
