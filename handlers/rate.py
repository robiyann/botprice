from pyrogram import filters
from pyrogram.types import Message
from bot import app
from mappings import symbol_to_id, vs_currency_mapping
import requests
import logging

def get_price(coin_id, vs_currency):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': vs_currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get(coin_id, {}).get(vs_currency, 0)

@app.on_message(filters.command("rate") & (filters.private | filters.group))
def rate_handler(client, message: Message):
    try:
        args = message.text.split()

        # Kasus: /rate 10 usdt idr
        if len(args) == 4:
            jumlah_token = float(args[1])
            coin_symbol = args[2].lower()
            vs_currency_symbol = args[3].lower()

        # Kasus: /rate 10 usdt (default ke IDR)
        elif len(args) == 3:
            jumlah_token = float(args[1])
            coin_symbol = args[2].lower()
            vs_currency_symbol = "idr"

        else:
            message.reply("Format salah! Contoh: /rate 10 usdt idr")
            return

        coin_id = symbol_to_id.get(coin_symbol, coin_symbol)
        vs_currency = vs_currency_mapping.get(vs_currency_symbol, vs_currency_symbol)

        price = get_price(coin_id, vs_currency)
        total_price = jumlah_token * price

        reply_text = f"Harga {jumlah_token} {coin_symbol.upper()} saat ini adalah {total_price:,.0f} {vs_currency.upper()}"
        message.reply(reply_text)

        logging.info(f"Handled /rate {jumlah_token} {coin_symbol} to {vs_currency} = {total_price:,.0f}")

    except Exception as e:
        logging.error(f"Error in rate_handler: {e}")
        message.reply(f"Terjadi error: {str(e)}")
