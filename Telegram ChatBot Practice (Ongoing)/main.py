from pprint import pprint

import constants as keys
from telegram.ext import *
import telepot
import responses as R
from telepot.loop import MessageLoop

print("bot started ")


def start_command(update, context):
    update.message.reply_text("type something")


def help_command(update, context):
    update.message.reply_text("no help sorry")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def handle(msg):
    pprint(msg)


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CommandHandler(Filters.text, handle_message))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('command', handle_message)],
        states={
            dp: [MessageHandler(Filters.text, handle_message)]
        },
        fallbakcs=[CommandHandler("stop", cancel)]
    )

    updater.start_polling()
    updater.idle()

main()






