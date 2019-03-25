import requests
from datetime import datetime


def format_datetime(timestamp):
    _dt = datetime.fromtimestamp(timestamp)
    return f"{_dt.day}/{_dt.month}/{_dt.year} - {_dt.hour}:{_dt.minute}"

def _get_top_news():
    '''
        returns an array of IDs for each hacker news story
    '''
    r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    data = r.json()
    return data

def _get_news_by_id(id):
    '''
        returns a news object given its ID 
    '''
    r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
    data = r.json()
    return data

def get_formatted_top_news(limit=None):
    top_news_ids = _get_top_news()
    news_list = []
    c = 0
    for id in top_news_ids:
        news = _get_news_by_id(id)
        news['time'] = format_datetime(news['time'])
        news_list.append(news)
        c += 1
        if limit and c > limit:
            break
    return news_list