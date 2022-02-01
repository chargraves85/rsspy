import sys
from pathlib import Path

from rsspy_backend.utils.nft_utils import NftFeedAnalyzer
import asyncio
import time


def run():
    nft_updater()


def nft_updater():

    start_time = time.time()
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    base_path = Path(__file__).parent
    file_path = (base_path / '../nft_utils/rss_feeds.txt').resolve()
    rss_file = open(file_path, 'r')
    feeds = rss_file.readlines()
    print("Make list from file --- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # coins = list(models.Coin.objects.all())
    # print("Get all objects --- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # CoinGather.CoinGather().update_model()
    # print("CoinGather --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    query_words = NftFeedAnalyzer.NftFeedAnalyzer(rss_feeds=feeds, max_connections=100).main()
    print(query_words)
    print("FeedAnalyzer --- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # BuzzScoreProcessor.BuzzScoreProcessor(coins).update_buzz_scores(query_words)
    # print("BuzzScoreProcessor --- %s seconds ---" % (time.time() - start_time))

