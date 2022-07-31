from pydoc import text
from telegram import Update,ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

updater = Updater(token='5355512939:AAGoOP16TsX022x-x_wPjYBaB5zF1rWYNNg')

def welcome(update: Update, context: CallbackContext):
    update.message.reply_text(f'Ассалому алайкум, {update.effective_user.full_name}. \nMoka.uz интернет бозорининг сотув ботига хуш келибсиз.')
    context.bot.send_message(chat_id=update.effective_user.id, text='Сиз кидираётган нарса бизда бор ва уни сиз "Каталог" оркали топишингиз мумкин😉')
def all_msg(update: Update, context: CallbackContext):
    update.message.reply_text(f'Илтимос "Каталог" оркали кидиринг)')
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', welcome))
dispatcher.add_handler(MessageHandler(Filters.all, all_msg))

updater.start_polling()
updater.idle()
