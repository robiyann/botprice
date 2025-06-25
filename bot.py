from pyrogram import Client
from config import api_id, api_hash, bot_token

app = Client(
    "simple_rate_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Import handlers
import handlers.rate
import handlers.help
import handlers.ping

if __name__ == "__main__":
    print("=== Simple Rate Bot Started ===")
    app.run()
