import requests
from datetime import datetime
from .exceptions import InvalidUsage
from typing import Optional, Any, List, Dict

def format_datetime(timestamp: float) -> str:
    """
        receive a timestamp and convert to a formated date string -> dd/MM/YYYY - hh:mm
    """
    _dt: datetime = datetime.fromtimestamp(timestamp)
    return f"{_dt.day}/{_dt.month}/{_dt.year} - {_dt.hour}:{_dt.minute}"

def _get_top_news() -> Optional[List[float]]:
    '''
        returns an array of IDs for each hacker news story
    '''
    r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    if r.status_code == 200:
        return r.json()
    return None

def _get_news_by_id(id: float) -> Optional[dict]:
    '''
        returns a news object given its ID 
    '''
    r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
    if r.status_code == 200:
        return r.json()
    return None

def get_formatted_top_news(limit:int=None) -> List[dict]:
    '''
        Returns a list of news as dictionaries
    '''
    top_news_ids: Optional[List[float]] = _get_top_news()
    
    # validate
    if not top_news_ids:
        raise InvalidUsage("We didn't find any hacker news this time, sorry", 404)

    news_list: List[dict] = []
    c: int = 0
    for id in top_news_ids:
        # get news by id
        news: Optional[dict] = _get_news_by_id(id)
        if news is not None:
            # format date
            news['time'] = format_datetime(news['time'])
            # append to dict
            news_list.append(news)

            c += 1
            if limit and c > limit:
                break

    return news_list