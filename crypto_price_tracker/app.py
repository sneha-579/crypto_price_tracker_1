# Folder structure
# crypto_price_tracker/
# ├── static/
# │   ├── style.css
# ├── templates/
# │   ├── index.html
# ├── app.py
# ├── requirements.txt

# app.py

from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(coin, currency="usd"):
    params = {"ids": coin, "vs_currencies": currency}
    response = requests.get(COINGECKO_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get(coin, {})
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    price_data = None
    coin = ""
    if request.method == "POST":
        coin = request.form.get("coin").lower()
        price_data = get_crypto_price(coin)
    return render_template("index.html", price_data=price_data, coin=coin)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port
    app.run(host="0.0.0.0", port=port)