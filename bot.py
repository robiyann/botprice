import logging
import sys
from pyrogram import Client
import handlers.rate  # Load handler
# Kalau ada help / ping: import juga
# import handlers.help
# import handlers.ping

# Load config
from config import api_id, api_hash, bot_token

# === SETUP LOGGING ===
log_file = "log.txt"

# Reset log.txt
with open(log_file, "w") as f:
    f.write("=== Simple Rate Bot Log Started ===\n")

# Setup logging ke file
logging.basicConfig(
    level=logging.DEBUG,  # Bisa ganti INFO kalau mau
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger()

# === START BOT ===
logger.info("=== Simple Rate Bot Starting ===")

app = Client(
    "simple_rate_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# === RUN ===
if __name__ == "__main__":
    try:
        logger.info("Connecting to Telegram API...")
        app.start()
        logger.info("Bot connected!")
        print("✅ Bot ready. Waiting for commands...")

        app.idle()  # keep running
    except Exception as e:
        logger.exception("Bot stopped due to error: %s", e)
    finally:
        app.stop()
        logger.info("Bot stopped. Exiting.")
