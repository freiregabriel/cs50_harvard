from flask import Blueprint, render_template, jsonify, request
from .settings import VERSION
from .exceptions import InvalidUsage, NoQuoteError
import requests
from typing import Optional, Any
lang = 'en'
format_ = 'json'
method = 'getQuote'
def get_quote() -> Optional[dict]:
    r = requests.get(f'http://api.forismatic.com/api/1.0/?lang={lang}&format={format_}&method={method}')
    if r.status_code == 200:
        return r.json()
    return None

# Blueprint
quotes_blueprint = Blueprint('quotes_blueprint', __name__, template_folder='templates')

# API
@quotes_blueprint.route("/quote", methods=["GET"])
def quote() -> Any:
    """
    Get random Quote
    """
    try:
        quote: Optional[dict] = get_quote()
        if not quote:
            raise InvalidUsage("No quote found this time, sorry", 404)
        return jsonify(quote)
    except NoQuoteError as e:
        raise e