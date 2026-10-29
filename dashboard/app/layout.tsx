import "./globals.css";


export const metadata = {

  title:
  "TITAN AI Trading Bot",

  description:
  "Autonomous AI Crypto Trading Intelligence System"

};



export default function RootLayout({

  children,

}: {

  children: React.ReactNode;

}) {


  return (

    <html lang="en">

      <body>

        {children}

      </body>

    </html>

  );

}
