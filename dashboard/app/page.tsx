import AIStatus from "@/components/AIStatus";
import MarketCard from "@/components/MarketCard";
import PositionCard from "@/components/PositionCard";
import WalletCard from "@/components/WalletCard";


export default function Home(){


return (

<main className="min-h-screen p-8">


<h1 className="text-4xl font-bold">

🔥 TITAN AI Trading Terminal

</h1>


<p className="mt-2 text-gray-400">

Autonomous AI Crypto Intelligence System

</p>



<div className="grid md:grid-cols-2 gap-6 mt-8">


<AIStatus />


<WalletCard />


<MarketCard />


<PositionCard />


</div>


</main>

)

}
