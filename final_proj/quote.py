import requests
from typing import Any

def get_quote() -> Any:
    r = requests.get('http://api.forismatic.com/api/1.0/?lang=en&format=json&method=getQuote')
    return r.json()