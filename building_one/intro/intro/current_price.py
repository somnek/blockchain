import requests

r = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
print(r.text)
