import datetime
import sys
from pathlib import Path

from rsspy_backend.utils.coin_utils import CoinGather, BuzzScoreProcessor, CoinFeedAnalyzer, CoinDataCleaner
import asyncio
from rsspy_backend import models
import time


def run():
    coin_updater()


def coin_updater():

    timestamp = datetime.datetime.now().timestamp()

    start_time = time.time()
    print("Starting list gather from file")
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    base_path = Path(__file__).parent
    file_path = (base_path / '../utils/coin_utils/rss_feeds.txt').resolve()
    rss_file = open(file_path, 'r')
    feeds = rss_file.readlines()
    print("Make list from file --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print("Starting CoinGather")
    CoinGather.CoinGather(timestamp).update_model()
    print("CoinGather --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print("Starting Getting Objects from DB")
    coins = list(models.Coin.objects.all())
    print("Get all objects --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print("Starting CoinFeedAnalyzer")
    results = CoinFeedAnalyzer.CoinFeedAnalyzer(feeds, coins, 100).main()
    print("FeedAnalyzer --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print("Starting BuzzScoreProcessor")
    BuzzScoreProcessor.BuzzScoreProcessor(coins, timestamp).update_buzz_scores(results)
    print("BuzzScoreProcessor --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print("Starting CoinDataCleaner")
    CoinDataCleaner.CoinDataCleaner(coins, timestamp, 7).clean_coin_data()
    print("CoinDataCleaner --- %s seconds ---" % (time.time() - start_time))

