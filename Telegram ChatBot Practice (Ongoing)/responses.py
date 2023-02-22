from datetime import datetime
import part_A
from telepot.loop import MessageLoop
import telepot

bot = telepot.Bot('5698107844:AAGIrr9D2l50vxj95Cdh6Ti3i97KjbAKRP0')
now = datetime.now()
date_time = now.strftime("%d/%m/%y, %H:%M:%S")


def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("start"):
        bot.sendMessage(str(date_time))
        return part_A.result

