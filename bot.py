import logging
import os

from pyrogram import Client
from config import api_id, api_hash, bot_token

LOG_FILE = "log.txt"
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

app = Client("simple_rate_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Load handlers
import handlers.ping
import handlers.help
import handlers.rate

if __name__ == "__main__":
    logging.info("=== Simple Rate Bot Starting ===")
    app.run()
