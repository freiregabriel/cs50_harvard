import requests
from typing import Optional
lang = 'en'
format_ = 'json'
method = 'getQuote'
def get_quote() -> Optional[dict]:
    r = requests.get(f'http://api.forismatic.com/api/1.0/?lang={lang}&format={format_}&method={method}')
    if r.status_code == 200:
        return r.json()
    return None