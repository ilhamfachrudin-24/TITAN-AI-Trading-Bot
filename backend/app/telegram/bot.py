import os


from telegram import Update

from telegram.ext import (

    Application,

    CommandHandler,

    ContextTypes

)



from app.telegram.commands import commands




TOKEN = os.getenv(

    "TELEGRAM_TOKEN"

)




async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    await update.message.reply_text(

        "🔥 TITAN AI Trading Bot Online"

    )





async def status(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    result = commands.status()



    await update.message.reply_text(

        str(result)

    )





async def start_bot(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    result = commands.start()



    await update.message.reply_text(

        str(result)

    )





async def stop_bot(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    result = commands.stop()



    await update.message.reply_text(

        str(result)

    )





def run_bot():


    app = Application.builder().token(

        TOKEN

    ).build()



    app.add_handler(

        CommandHandler(
            "start",
            start_bot
        )

    )


    app.add_handler(

        CommandHandler(
            "status",
            status
        )

    )


    app.add_handler(

        CommandHandler(
            "stop",
            stop_bot
        )

    )


    app.run_polling()
