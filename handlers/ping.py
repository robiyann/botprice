# handlers/ping.py
from pyrogram import filters

def register_ping(app):
    @app.on_message(filters.command("ping"))
    def ping_handler(client, message):
        message.reply("pong")
