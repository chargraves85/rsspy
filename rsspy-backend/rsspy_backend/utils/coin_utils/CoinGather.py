import pprint

from pycoingecko import CoinGeckoAPI
from rsspy_backend.models import Coin


class CoinGather:

    def __init__(self, timestamp):
        self.cg = CoinGeckoAPI()
        self.timestamp = timestamp

    def build_coin_data(self):
        coins = []
        categories = ['cryptocurrency', 'binance-smart-chain']
        for category in categories:
            next_page = True
            page = 0
            while next_page is True:
                coin_data = self.cg.get_coins_markets(vs_currency='usd', category=category, page=page, per_page=250)
                for data in coin_data:
                    if not data['current_price']:
                        continue
                    if data['current_price'] is None or (data['current_price'] <= 0):
                        continue
                    if data['market_cap'] is None or (data['market_cap'] <= 0):
                        continue
                    if data['circulating_supply'] is None or (data['current_price'] <= 0):
                        continue
                    coins.append(
                        {
                            'coinName': data['name'],
                            'symbol': data['symbol'],
                            'timestamp': self.timestamp,
                            'value': data['current_price']
                        }
                    )
                page += 1

                if not coin_data:
                    next_page = False

        return coins

    # TODO: make async
    def update_model(self):
        coins = self.build_coin_data()
        for coin in coins:

            if Coin.objects.filter(coinName__exact=coin['coinName']).exists():
                coin_data = Coin.objects.get(coinName__exact=coin['coinName'])
                coin_data.data[coin['timestamp']] = {'value': coin['value']}
                coin_data.coinName = coin['coinName']
                coin_data.symbol = coin['symbol']
                coin_data.save()

            else:
                new_coin = Coin(
                    coinName=coin['coinName'],
                    symbol=coin['symbol'],
                    data={coin['timestamp']: {'value': coin['value']}}
                )
                new_coin.save()
