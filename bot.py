import requests
import logging
from telegram import *
from telegram.ext import *
import os

PORT = int(os.environ.get('PORT', 5000))


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "1355356462:AAFGOK3rX5_uqKO0BxCPEqvjakIYi9o8XxU"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"""*Hi {update.effective_chat.first_name},* 

Welcome to the Torrent Searcher Bot. Here you will find all the torrents you search for...

Type /help to know how to use the bot.

Type /info to know about the developer.""", parse_mode=ParseMode.MARKDOWN)

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""Hey, this is not most complicated bot. Just send me the query you want to search and i will do the rest!

This bot is in the *BETA* stage. So, if any error occurs, feel free to pm me on @cosmicpredator""", parse_mode=ParseMode.MARKDOWN)


def torr_serch(update: Update, context: CallbackContext) -> None:
    try:
        update.message.reply_text("Searching results for {}".format(update.message.text))
        url = "https://api.sumanjay.cf/torrent/?query={}".format(update.message.text)
        results = requests.get(url).json()
        print(results)
        for item in results:
            age = item.get('age')
            leech = item.get('leecher')
            mag = item.get('magnet')
            name = item.get('name')
            seed = item.get('seeder')
            size = item.get('size')
            typ= item.get('type')
            update.message.reply_text(f"""*Name:* {name}
_Uploaded {age} ago_
*Seeders:* `{seed}`
*Leechers:* `{leech}`
*Size:* `{size}`
*Type:* {typ}
*Magnet Link:* `{mag}`""", parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text("End of the search results...")
    except:
        update.message.reply_text("""Search results completed...
If you've not seen any results, try researching...!""")


def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""*Made with ❤️ in India by @cosmicpredator.*

*Language:* [Python3](https://www.python.org/)

*Bot Framework:* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)

*Server:* [Heroku](www.heroku.com)

*Source Code:* `Sore ga kuru made matsu`

If you 👍 this bot, Support the developer by just sharing the bot to Your friends...""", parse_mode=ParseMode.MARKDOWN)


def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), torr_serch))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://protected-shelf-35703.herokuapp.com/' + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()









