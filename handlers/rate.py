import logging
from pyrogram import Client
from config import api_id, api_hash, bot_token

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt", mode='w'),  # hapus & buat baru
        logging.StreamHandler()
    ]
)

# Create app
app = Client("simple_rate_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Import handlers
import handlers.ping
import handlers.help
import handlers.rate

# Start bot
logging.info("=== Simple Rate Bot Starting ===")
app.start()
logging.info("Bot connected!")
print("✅ Bot ready. Waiting for commands...")

# Keep running
try:
    app.run()
except Exception as e:
    logging.error(f"Bot stopped due to error: {e}")

app.stop()
logging.info("Bot stopped. Exiting.")
