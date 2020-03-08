from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import bot_settings
from handlers import *


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(bot_settings.API_KEY, request_kwargs=bot_settings.PROXY, use_context=False)

    logging.info("Бот запускается")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_pic, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('Send cat'), send_cat_pic, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('^(Change avatar)$'), change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()


main()