from pyrogram import filters
from bot import app
from mappings import symbol_to_id, vs_currency_mapping
import requests

DEFAULT_VS_CURRENCY = 'idr'

def get_price(coin_id, vs_currency):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': coin_id,
        'vs_currencies': vs_currency
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get(coin_id, {}).get(vs_currency, 0)

@app.on_message(filters.command("rate"))
def rate_handler(client, message):
    try:
        args = message.text.strip().split()

        if len(args) < 3:
            message.reply("Format salah! Contoh: /rate 10 usdt [idr/usd/...]")
            return

        jumlah_token = float(args[1])
        coin_symbol = args[2].lower()

        # jika ada arg ke-4, pakai sebagai vs_currency
        if len(args) >= 4:
            vs_currency_symbol = args[3].lower()
        else:
            vs_currency_symbol = DEFAULT_VS_CURRENCY  # default ke idr

        coin_id = symbol_to_id.get(coin_symbol, coin_symbol)
        vs_currency = vs_currency_mapping.get(vs_currency_symbol, vs_currency_symbol)

        price = get_price(coin_id, vs_currency)
        total_price = jumlah_token * price

        reply_text = (
            f"Harga {jumlah_token} {coin_symbol.upper()} "
            f"saat ini adalah {total_price:,.0f} {vs_currency.upper()}"
        )
        message.reply(reply_text)

    except Exception as e:
        message.reply(f"Terjadi error: {str(e)}")
