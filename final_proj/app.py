from cs50 import SQL
from flask import Flask, render_template, redirect, request, jsonify, Response, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from .exceptions import NoPokemonNameError, InvalidPokemonNameError, NoQuoteError, YoutubeError, InvalidUsage
from .pokemon import get_pokemon, Pokemon
from .quote import get_quote
from .chuck import get_chuck_joke
from .youtube import download_video
from .hackernews import get_formatted_top_news
from .settings import VERSION
from datetime import datetime
from typing import Any, Optional, Dict

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
version: str = VERSION

# Date filter
def format_datetime(timestamp: int) -> str:
    _dt = datetime.fromtimestamp(timestamp)
    return f"{_dt.day}/{_dt.month}/{_dt.year}"

app.jinja_env.filters['datetime'] = format_datetime

# Ensure responses aren't cached
@app.after_request
def after_request(response:Any) -> Any:
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db: SQL = SQL("sqlite:///utilities.db")

# Error handling
def apology(name: Optional[str], description: Optional[str], code: Optional[int]) -> dict:
    """
    handle error as JSON
    """
    response = jsonify({
        "name": name,
        "description": description,
        "code": code
    })
    response.status_code = code
    return response

def render_with_version(templateUrl: str):
    """
    reusable function to render template aways passing the current application version
    """
    return render_template(templateUrl, version=version)

# Pages
@app.route("/")
def index() -> Any:
    """Show portfolio of stocks"""
    return render_with_version("index.html")

@app.route("/dogs")
def dogs() -> Any:
    """
    dogs page
    """
    return render_with_version("dogs.html")

@app.route("/cats")
def cats() -> Any:
    """
    cats page
    """
    return render_with_version("cats.html")

@app.route("/pokemon_index")
def pokemon_page() -> Any:
    """
    pokemon page
    """
    return render_with_version("pokemon.html")

@app.route("/country_finder_by_ip")
def ip() -> Any:
    """
    ip page
    """
    return render_with_version("ip.html")

@app.route("/chuck_norris_jokes")
def chuck_page() -> Any:
    """
    chuck page
    """
    return render_with_version("chuck.html")

@app.route("/youtube_video_downloader")
def youtube_page() -> Any:
    """
    youtube page
    """
    return render_with_version("youtube.html")

@app.route("/quick_hacker_news")
def hackernews_page() -> Any:
    """
    hacker news page
    """
    return render_with_version("hackernews.html")

# REST Apis
@app.route("/api_hacker_news", methods=['GET'])
def hackernews_api() -> Any:
    """
    Load hacker news stories
    """
    try:
        # will return up to 5 news stories
        news = get_formatted_top_news(limit=5)
        return jsonify(news)
    except HTTPException as e:
        raise e

@app.route("/pokemon", methods=["GET"])
def pokemon() -> Any:
    """
    Get pokemon details by name
    """
    name: Optional[str] = request.args.get('name')
    try:
        if not name:
            raise InvalidUsage("No pokemon name was passed", 400)
        pokemon: dict = get_pokemon(name)
        return jsonify(pokemon)
    except InvalidPokemonNameError as e:
        raise e

@app.route("/quote", methods=["GET"])
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

@app.route("/chuck", methods=["GET"])
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

@app.route('/download', methods=["GET"])
def download_by_id() -> Any:
    """
    Download an youtube video
    """
    try:
        url: Optional[str] = request.args.get('url')

        # validate
        if not url:
            raise InvalidUsage("No URL was passed", 400)

        # get video binary and video title from youtube api
        binary, title = download_video(url)

        # validate
        if not binary or not title:
            raise YoutubeError()

        return Response(binary, headers={'Content-Disposition': 'attachment; '
                                        'filename=' + f"{title}.mp4"})
    except YoutubeError as e:
        raise e

@app.errorhandler(HTTPException)
def errorhandler(e: HTTPException) -> Any:
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()

    return apology(e.name, e.description, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
