from flask import Blueprint, render_template, jsonify, request
from .settings import VERSION
from .exceptions import InvalidUsage, NoQuoteError
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

# Blueprint
chuck_blueprint = Blueprint('chuck_blueprint', __name__, template_folder='templates')

# Page
@chuck_blueprint.route("/chuck_norris_jokes")
def chuck_page() -> Any:
    """
    chuck page
    """
    return render_template("chuck.html", version=VERSION)

# API
@chuck_blueprint.route("/chuck", methods=["GET"])
def chuck_joke() -> Any:
    """
    Get random Chuck Norris joke
    """
    try:
        quote = get_chuck_joke()

        if not quote:
            raise InvalidUsage("Sorry, no quote found this time", 404)

        return jsonify(quote)

    except NoQuoteError as e:
        raise e