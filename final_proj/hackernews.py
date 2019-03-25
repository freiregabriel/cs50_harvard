import requests
from datetime import datetime
from typing import Optional, Any, List, Dict

def format_datetime(timestamp: float) -> str:
    _dt: datetime = datetime.fromtimestamp(timestamp)
    return f"{_dt.day}/{_dt.month}/{_dt.year} - {_dt.hour}:{_dt.minute}"

def _get_top_news() -> List[float]:
    '''
        returns an array of IDs for each hacker news story
    '''
    r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    data = r.json()
    return data

def _get_news_by_id(id: float) -> Dict[Any,Any]:
    '''
        returns a news object given its ID 
    '''
    r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
    data = r.json()
    return data

def get_formatted_top_news(limit:int=None) -> List[Dict[str,Any]]:
    top_news_ids: List[float] = _get_top_news()
    news_list: List[Dict[str, Any]] = []
    c: int = 0
    for id in top_news_ids:
        news: Dict[Any,Any] = _get_news_by_id(id)
        news['time'] = format_datetime(news['time'])
        news_list.append(news)
        c += 1
        if limit and c > limit:
            break
    return news_list