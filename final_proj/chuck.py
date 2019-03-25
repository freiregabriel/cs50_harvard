import requests
from typing import Dict, Any

def get_chuck_joke() -> Dict[str, str]:
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data: Dict[Any, Any] = r.json()
    final: Dict[str, str] = {}
    final['icon_url'] = data['icon_url']
    final['value'] = data['value']
    return final