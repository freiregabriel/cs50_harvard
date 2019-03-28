import requests
from typing import Dict, Any, Optional

api = 'https://api.chucknorris.io/jokes/random'
def get_chuck_joke() -> Optional[dict]:
    # http req
    r = requests.get(api)
    if r.status_code == 200:
        data: dict = r.json()

        # i don't want all the data that comes from the api
        final: dict = {}
        final['icon_url'] = data['icon_url']
        final['value'] = data['value']
        return final
    return None