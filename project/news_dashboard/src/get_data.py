import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import pytz
from fake_useragent import UserAgent

from src.preprocess_data import tokenize


class News:
    def __init__(self):
        self.request = requests.session()

    def get_channel(self):
        user_agent = UserAgent()
        url = 'https://news.naver.com/main/ranking/popularDay.naver'
        res = self.request.get(url, headers={'User-Agent': user_agent.random})
        soup = BeautifulSoup(res.text, 'html.parser')

        channel_ids = soup.find_all('a', class_='rankingnews_box_head')
        channel_name = soup.find_all('strong', class_='rankingnews_name')

        channels = {}

        for (idx, name) in zip(channel_ids, channel_name):
            channels[str(re.search(r'press/(\d{3})/', idx['href']).group(1))] = name.text
        return channels

    def get_popular_news(self, channel):
        # 많이 본 뉴스
        news_link = []
        url = f'https://media.naver.com/press/{channel}/ranking?type=popular'
        res = self.request.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        hot_news = soup.find_all('a', class_='_es_pc_link')

        for news in hot_news:
            news_link.append(news['href'])
        return news_link

    def get_title_and_tag(self, link, channel):
        res = self.request.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find('meta', property='og:title').get('content')

        categorize_item = soup.find('em', class_='media_end_categorize_item')
        category_text = ''
        if categorize_item:
            category_text = categorize_item.get_text(strip=True)
        return {'title': title,
                'tags': tokenize(title),
                'category': category_text,
                '@timestamp': datetime.now(pytz.timezone('Asia/Seoul')).isoformat(),
                'url': link,
                'channel': channel}
