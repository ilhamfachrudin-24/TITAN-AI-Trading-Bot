import AIStatus from "@/components/AIStatus";
import MarketCard from "@/components/MarketCard";
import PositionCard from "@/components/PositionCard";
import WalletCard from "@/components/WalletCard";
import LiveTradingPanel from "@/components/LiveTradingPanel";
import MarketStream from "@/components/MarketStream";



export default function Home(){


return (

<main className="
min-h-screen
p-8
">


<h1 className="
text-4xl
font-bold
">

🔥 TITAN AI Trading Terminal

</h1>



<p className="
text-gray-400
mt-2
">

Autonomous AI Crypto Intelligence System

</p>




<div className="
grid
md:grid-cols-2
gap-6
mt-8
">


<AIStatus />


<WalletCard />


<MarketCard />


<PositionCard />


</div>




<div className="
mt-8
">


<LiveTradingPanel />


</div>



</main>

)

}
