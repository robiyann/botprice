import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from pyrogram import Client
from config import api_id, api_hash, bot_token

app = Client(
    "simple_rate_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Import handlers (sesuai folder Anda: botprice/handlers/*.py)
import handlers.rate
import handlers.help
import handlers.ping

if __name__ == "__main__":
    print("=== Simple Rate Bot Started ===")
    app.run()
