from pyrogram import filters
from bot import app
from mappings import symbol_to_id, vs_currency_mapping
import requests

def get_price(coin_id, vs_currency):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': vs_currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get(coin_id, {}).get(vs_currency, 0)

@app.on_message(filters.command("rate") & (filters.chat_type.groups | filters.chat_type.private))
def rate_handler(client, message):
    try:
        args = message.text.split()
        if len(args) != 4:
            message.reply("Format salah! Contoh: /rate 10 usdt idr")
            return

        jumlah_token = float(args[1])
        coin_symbol = args[2].lower()
        vs_currency_symbol = args[3].lower()

        coin_id = symbol_to_id.get(coin_symbol, coin_symbol)
        vs_currency = vs_currency_mapping.get(vs_currency_symbol, vs_currency_symbol)

        price = get_price(coin_id, vs_currency)
        total_price = jumlah_token * price

        reply_text = f"Harga {jumlah_token} {coin_symbol.upper()} saat ini adalah {total_price:,.0f} {vs_currency.upper()}"
        message.reply(reply_text)

    except Exception as e:
        message.reply(f"Terjadi error: {str(e)}")
