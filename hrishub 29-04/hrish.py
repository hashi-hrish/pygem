import requests
import json
import time
import hmac
import hashlib
import base64

#Replace with your actual API key and secret
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'.encode()

BASE_URL = 'http://api.gemini.com'

# ===Public API Example: Get Ticket for BTC/USD ===
def get_ticker(symbol='btcusd'):
    url = f"{BASE_URL/v1/pubticker/{symbol}"
    return response.json()


# === Run Sample ===
if __name__ == '__main__':
    print("== BTC/USD Ticker ==")
    print(get_ticker())

    print("\n== Account Balances ==")
    print(get_account_balance())