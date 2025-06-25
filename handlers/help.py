from pyrogram import filters
from bot import app

@app.on_message(filters.command("help") & (filters.private | filters.group))
def help_handler(client, message):
    help_text = (
        "**Simple Rate Bot**\n\n"
        "Command:\n"
        "/rate jumlah coin vs_currency\n"
        "contoh: /rate 10 usdt idr\n"
        "/ping - cek bot online\n"
        "/help - tampilkan bantuan"
    )
    message.reply(help_text)
