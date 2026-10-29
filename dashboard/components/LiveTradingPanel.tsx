"use client"


import {
    useTitan
}
from "@/hooks/useTitan"



export default function LiveTradingPanel(){


    const {
        system,
        bot
    } = useTitan()



return (

<div className="
border
rounded-xl
p-6
space-y-4
">


<h2 className="
text-2xl
font-bold
">

⚡ TITAN AI Live Monitor

</h2>



<div>


<p>

System:

</p>


<pre>

{JSON.stringify(
    system,
    null,
    2
)}

</pre>


</div>




<div>


<p>

Auto Trading:

</p>


<pre>

{JSON.stringify(
    bot,
    null,
    2
)}

</pre>


</div>



</div>

)

}
