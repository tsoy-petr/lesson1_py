from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(bot, update):
    print('Вызван start')
    update.message.reply_text('Вызван start')

def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()    