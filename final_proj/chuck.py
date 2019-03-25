import requests

def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    final = {}
    final['icon_url'] = data['icon_url']
    final['value'] = data['value']
    return final