from pathlib import Path

import feedparser
from bs4 import BeautifulSoup
import aiohttp
from aiohttp.client import ClientSession
import asyncio


class NftFeedAnalyzer:

    def __init__(self, rss_feeds, max_connections):
        base_path = Path(__file__).parent
        file_path = (base_path / '../stop_words.txt').resolve()
        self.stop_words = open(file_path, 'r').readlines()
        self.conns = max_connections
        self.query_text = ''
        self.web_links = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/56.0.2924.76 Safari/537.36'}
        asyncio.run(self.parse_all_feeds(rss_feeds))
        asyncio.run(self.scrape_all_rss())
        print('Attempting to crawl through ' + str(len(self.web_links)) + ' articles.')

    async def scrape_rss(self, url, session: ClientSession):
        async with session.get(url) as response:
            result = await response.text()
            soup = BeautifulSoup(result, "html.parser")
            paragraphs = soup.find_all('p')
            raw_text = ""
            for para in paragraphs:
                raw_text += para.getText()
                raw_text = raw_text.encode("ascii", 'ignore')
                self.query_text += raw_text.decode("utf-8")

    async def parse_feed(self, url, session: ClientSession):
        async with session.get(url) as response:
            feed_obj = feedparser.parse(await response.text())
            for link in feed_obj["items"]:
                self.web_links.append(link["link"])

    async def parse_all_feeds(self, feeds):

        my_conn = aiohttp.TCPConnector(limit=self.conns)
        async with aiohttp.ClientSession(connector=my_conn, headers=self.headers) as session:
            tasks = []
            for url in feeds:
                try:
                    task = asyncio.ensure_future(self.parse_feed(url=url, session=session))
                    tasks.append(task)
                except ValueError as e:
                    print("Error on : ", url)
                    print(e)
                    continue
            await asyncio.gather(*tasks, return_exceptions=True)

    async def scrape_all_rss(self):
        my_conn = aiohttp.TCPConnector(limit=self.conns)
        async with aiohttp.ClientSession(connector=my_conn, headers=self.headers) as session:
            tasks = []
            for url in self.web_links:
                try:
                    task = asyncio.ensure_future(self.scrape_rss(url=url, session=session))
                    tasks.append(task)
                except ValueError as e:
                    print("Error on : ", url)
                    print(e)
                    continue
            await asyncio.gather(*tasks, return_exceptions=True)

    def main(self):
        # Count occurrences of keyword
        result_words = []
        query_split = self.query_text.split()

        for word in query_split:
            if word.lower() not in [counted_word_lower.lower() for counted_word_lower in self.stop_words]:
                result_words.append(word)
            else:
                continue

        return result_words
