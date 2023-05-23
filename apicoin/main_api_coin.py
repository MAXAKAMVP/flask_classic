import requests

API_KEY = "A055EF56-5D39-4CE3-BDE4-44D71E7BE2D1"
#coin_to = "BTC"

def get_rate(coin_to):
    url = 'https://rest.coinapi.io/v1/exchangerate/EUR/{coin_to}'
    headers = {'X-CoinAPI-Key' : API_KEY}
    response = requests.get(url, headers=headers)
    reply = response.json()
    rate = reply["rate"]

    print(rate)

get_rate("BTC")



