import feedparser
from bs4 import BeautifulSoup
import aiohttp
from aiohttp.client import ClientSession
import asyncio


class CoinFeedAnalyzer:

    def __init__(self, rss_feeds, analyzed_coins, max_connections):
        self.keywords = analyzed_coins
        self.conns = max_connections
        self.query_text = []
        self.web_links = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/56.0.2924.76 Safari/537.36'}
        asyncio.run(self.parse_all_feeds(rss_feeds))
        asyncio.run(self.scrape_all_rss())

    async def scrape_rss(self, url, session: ClientSession):
        async with session.get(url) as response:
            result = await response.text()
            soup = BeautifulSoup(result, "html.parser")
            paragraphs = soup.find_all('p')
            raw_text = ""
            for para in paragraphs:
                raw_text += para.getText()
                raw_text = raw_text.encode("ascii", 'ignore')
                self.query_text.append(raw_text.decode("utf-8"))

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

        results = {}

        # TODO: Perhaps do article loop first and add to dict as we go to speed up loop
        for keyword in self.keywords:
            total_article_count = 0
            total_buzz = 0
            for article in self.query_text:
                words = [words.lower() for words in article.split()]
                if keyword.coinName.lower() in words:
                    total_article_count += 1
                buzz = words.count(keyword.coinName.lower())
                total_buzz += buzz
                buzz_plural = words.count(keyword.coinName.lower() + 's')
                total_buzz += buzz_plural
            if total_buzz > 0:
                results[keyword.coinName.lower()] = {'buzz': total_buzz, 'articles': total_article_count}

        return results
