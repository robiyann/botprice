# bot.py

import logging
from pyrogram import Client
from config import api_id, api_hash, bot_token

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt", mode="w"),
        logging.StreamHandler()
    ]
)

# Init bot client
app = Client("simple_rate_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Register handlers
from handlers.ping import register_ping
from handlers.help import register_help
from handlers.rate import register_rate

register_ping(app)
register_help(app)
register_rate(app)

# Run bot
logging.info("✅ Bot connected! Waiting for commands...")
app.run()
