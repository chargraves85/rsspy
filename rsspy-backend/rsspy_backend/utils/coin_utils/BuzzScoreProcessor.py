from collections import OrderedDict

from pycoingecko import CoinGeckoAPI

from rsspy_backend.models import Coin


class BuzzScoreProcessor:

    def __init__(self, coins, timestamp):
        self.cg = CoinGeckoAPI()
        self.coins = coins
        self.timestamp = timestamp

    def update_buzz_scores(self, results):
        for coin in list(self.coins):

            data_prop_counter = list(coin.data.keys())

            if len(data_prop_counter) == 1:
                control = Coin.objects.get(coinName='Bitcoin')
                keys = list(control.data.keys())
                for key in keys:
                    if coin.data[key]:
                        coin.data[key].update({'buzzScore': 0, 'articleCount': 0})
                    else:
                        coin.data[key] = {'buzzScore': 0, 'articleCount': 0}

                coin.save()

            if str(self.timestamp) not in coin.data:
                coin.data[str(self.timestamp)] = {'value': 'unknown'}

            if coin.coinName.lower() in results:

                new_score = results[coin.coinName.lower()]['buzz']
                new_article_count = results[coin.coinName.lower()]['articles']
                coin.previousBuzzScore = coin.currentBuzzScore
                coin.currentBuzzScore = new_score
                coin.data[str(self.timestamp)].update({'buzzScore': new_score, 'articleCount': new_article_count})

            else:
                new_score = 0
                new_article_count = 0
                coin.data[str(self.timestamp)].update({'buzzScore': new_score, 'articleCount': new_article_count})
                coin.previousBuzzScore = coin.currentBuzzScore
                coin.currentBuzzScore = new_score

            # coin.save()

