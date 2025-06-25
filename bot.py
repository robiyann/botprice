import os
import logging
from pyrogram import Client
import handlers.ping
import handlers.help
import handlers.rate
import config

# Setup logging
LOG_FILE = "log.txt"
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

logging.basicConfig(
    level=logging.DEBUG,  # bisa diganti INFO jika mau lebih singkat
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

# Create Pyrogram Client
app = Client(
    "simple_rate_bot",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)

# Main loop
if __name__ == "__main__":
    try:
        logger.info("=== Simple Rate Bot Starting ===")
        with app:
            logger.info("Bot connected!")
            print("✅ Bot ready. Waiting for commands...")
            app.run()
    except Exception as e:
        logger.exception("Bot stopped due to error: %s", e)
    finally:
        logger.info("Bot stopped. Exiting.")
