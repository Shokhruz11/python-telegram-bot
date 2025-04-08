from telegram import Bot
from telegram.ext import Updater, CommandHandler

# 7942274515:AAFHR75qEHbAOrH2oFdGLXpohHwRc2rknII
TOKEN = '7942274515:AAFHR75qEHbAOrH2oFdGLXpohHwRc2rknII'

def start(update, context):
    update.message.reply_text("Salom! Men yangi botman!")

def main():
    # Botni ishga tushirish
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # /start komandasini qayta ishlash
    dp.add_handler(CommandHandler("start", start))

    # Botni ishlashini boshlash
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
