# Telegram Bot (Python)
Telegram bot built with python-telegram-bot.
## Local Development

    cp .env.example .env
    # Add your bot token from @BotFather
    pip install -r requirements.txt
    python bot.py

## Adding Handlers
Add command and message handlers in handlers/. See handlers/commands.py.
## Deploy on StackBlaze
This template includes a stackblaze.yaml. Set TELEGRAM_BOT_TOKEN.
