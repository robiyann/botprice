from pyrogram import filters
from bot import app

@app.on_message(filters.command("ping") & (filters.private | filters.group))
def ping_handler(client, message):
    message.reply("✅ Bot is online!")
