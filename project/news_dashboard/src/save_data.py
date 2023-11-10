from src.get_data import News
from es.connection import ES


def save_to_es():
    news = News()
    es = ES("http://34.64.93.25:9200").client

    channels = news.get_channel()
    for idx, name in channels.items():
        news_links = news.get_popular_news(idx)
        for news_link in news_links:
            data = news.get_title_and_tag(news_link, name)
            response = es.index(index='news', body=data)
