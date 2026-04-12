import os
from dotenv import load_dotenv
from telegram.ext import Application
from handlers.commands import start, help_command, echo

load_dotenv()


def main():
    app = Application.builder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()

    app.add_handler(start)
    app.add_handler(help_command)
    app.add_handler(echo)

    print("Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
