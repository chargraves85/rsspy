import datetime
import copy


class CoinDataCleaner:

    def __init__(self, coins, timestamp, delta):  # TODO: delta should be an env var
        self.coins = coins
        self.timestamp = timestamp
        self.delta = delta

    def clean_coin_data(self):
        for coin in list(self.coins):
            timestamps = coin.data.keys()

            for timestamp in copy.copy(list(timestamps)):
                delta = datetime.datetime.fromtimestamp(self.timestamp) - datetime.timedelta(self.delta)

                if datetime.datetime.fromtimestamp(float(timestamp)) < delta:
                    coin.data.pop(str(timestamp))

            coin.save()
