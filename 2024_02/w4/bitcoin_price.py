import urllib.request
import json
import datetime


def get_bitcoin_price(days_back):
    date = datetime.datetime.now() - datetime.timedelta(days=days_back)
    date_str = date.strftime('%d-%m-%Y')

    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={date_str}'

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    price_usd = data['market_data']['current_price']['usd']
    return price_usd


# print(get_bitcoin_price(5))