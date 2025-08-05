from flask import Flask, render_template, request
import requests

app = Flask(__name__)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

SUPPORTED_CURRENCIES = ["usd", "inr", "eur", "gbp", "jpy", "aud", "cad"]

def get_token_id(user_input):
    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/list")
        if response.status_code == 200:
            coins = response.json()
            user_input = user_input.lower()
            for coin in coins:
                if coin['symbol'].lower() == user_input or coin['id'].lower() == user_input:
                    return coin['id']
    except Exception as e:
        print("Error fetching token list:", e)
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    price = None
    token_input = ""
    currency = "usd"
    error = ""

    if request.method == "POST":
        token_input = request.form.get("token", "").strip()
        currency = request.form.get("currency", "usd").lower()
        token_id = get_token_id(token_input)

        if token_id:
            params = {
                "ids": token_id,
                "vs_currencies": currency
            }
            response = requests.get(f"{COINGECKO_API_URL}/simple/price", params=params)
            if response.status_code == 200:
                data = response.json()
                try:
                    price = data[token_id][currency]
                except KeyError:
                    error = f"❌ Conversion to '{currency.upper()}' not available."
            else:
                error = "❌ Failed to fetch price from API."
        else:
            error = "❌ Token not found. Please enter a valid symbol or name."

    return render_template(
        "index.html",
        price=price,
        token=token_input.upper(),
        currency=currency.upper(),
        error=error,
        currencies=SUPPORTED_CURRENCIES
    )


if __name__ == "__main__":
    app.run(debug=True)
