# handlers/help.py
from pyrogram import filters

def register_help(app):
    @app.on_message(filters.command("help"))
    def help_handler(client, message):
        text = (
            "Daftar Perintah:\n"
            "/ping - Cek bot online\n"
            "/help - Bantuan\n"
            "/rate <jumlah> <token> <currency> - Cek harga koin\n"
        )
        message.reply(text)
