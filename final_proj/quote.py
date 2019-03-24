import requests

def get_quote():
    r = requests.get('http://api.forismatic.com/api/1.0/?lang=en&format=json&method=getQuote')
    return r.json()