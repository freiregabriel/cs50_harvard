from flask import Blueprint, render_template, jsonify, request
from .settings import VERSION
from concurrent.futures import ThreadPoolExecutor
import asyncio
import requests
from werkzeug.exceptions import HTTPException
from datetime import datetime
from .exceptions import InvalidUsage
from typing import Optional, Any, List, Dict

def format_datetime(timestamp: float) -> str:
    """ receive a timestamp and convert to a formated date string -> dd/MM/YYYY - hh:mm """
    _dt: datetime = datetime.fromtimestamp(timestamp)
    return f"{_dt.day}/{_dt.month}/{_dt.year} - {_dt.hour}:{_dt.minute}"

def _get_top_news() -> Optional[List[float]]:
    ''' returns an array of IDs for each hacker news story '''
    r = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    if r.ok:
        return r.json()
    return None

def _get_news_by_id(id: float, session: requests.Session) -> Optional[dict]:
    ''' returns a news object given its ID '''
    r = session.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
    if r.ok:
        return r.json()
    return None

async def get_formatted_top_news(limit:int=None) -> List[dict]:
    ''' Returns a list of news as dictionaries '''
    top_news_ids: Optional[List[float]] = _get_top_news()
    
    # validate
    if not top_news_ids:
        raise InvalidUsage("We didn't find any hacker news this time, sorry", 404)

    news_list: List[dict] = []
    c: int = 0

    # get news by ID asynchronously
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(executor, _get_news_by_id, 
                                    *(id, session)) for id in top_news_ids[:limit]
            ]
            for response in await asyncio.gather(*tasks):
                response['time'] = format_datetime(response['time'])
                news_list.append(response)

    return news_list

# Blueprint
hackernews_blueprint = Blueprint('hackernews_blueprint', __name__, template_folder='templates')

# Page
@hackernews_blueprint.route("/quick_hacker_news")
def hackernews_page() -> Any:
    """ hacker news page """
    return render_template("hackernews.html", version=VERSION)

# API
@hackernews_blueprint.route("/api_hacker_news", methods=['GET'])
def hackernews_api() -> Any:
    """ Load hacker news stories """
    try:
        # will return up to 5 news stories

        # crete new event loop to avoid "RuntimeError: There is no current event loop in thread 'Thread-8'."
        asyncio.set_event_loop(asyncio.new_event_loop())

        # get loop
        loop = asyncio.get_event_loop()
        
        # ensure request will be properly done
        future = asyncio.ensure_future(get_formatted_top_news(limit=10))
        
        # run requests asynchronously
        news = loop.run_until_complete(future)
        loop.close()
        return jsonify(news)
    except HTTPException as e:
        raise e