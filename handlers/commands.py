from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ContextTypes, filters


async def _start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot.")


async def _help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Start the bot\n/help - Show help")


async def _echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


start = CommandHandler("start", _start)
help_command = CommandHandler("help", _help)
echo = MessageHandler(filters.TEXT & ~filters.COMMAND, _echo)
