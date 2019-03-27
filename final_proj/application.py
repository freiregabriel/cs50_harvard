from flask import Flask, render_template, redirect, request, jsonify, Response
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from pokemon import get_pokemon, Pokemon
from quote import get_quote
from chuck import get_chuck_joke
from youtube import download_video
from hackernews import get_formatted_top_news
from settings import VERSION
from datetime import datetime
from typing import Any, Optional, Dict

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
version: str = VERSION

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

def apology(name: Optional[str], code: Optional[int]) -> Any:
    return render_template('error.html', version=version, name=name, code=code)

# Pages
@app.route("/")
def index() -> Any:
    """Show portfolio of stocks"""
    return render_template("index.html", version=version)

@app.route("/dogs")
def dogs() -> Any:
    return render_template("dogs.html", version=version)

@app.route("/cats")
def cats() -> Any:
    return render_template("cats.html", version=version)

@app.route("/pokemon_index")
def pokemon_page() -> Any:
    return render_template("pokemon.html", version=version)

@app.route("/country_finder_by_ip")
def ip() -> Any:
    return render_template("ip.html", version=version)

@app.route("/chuck_norris_jokes")
def chuck_page() -> Any:
    return render_template("chuck.html", version=version)

@app.route("/youtube_video_downloader")
def youtube_page() -> Any:
    return render_template("youtube.html", version=version)

@app.route("/quick_hacker_news")
def hackernews_page() -> Any:
    return render_template("hackernews.html", version=version)

# REST Apis
@app.route("/api_hacker_news", methods=['GET'])
def hackernews_api() -> Any:
    try:
        news = get_formatted_top_news(limit=5)
        return jsonify(news)
    except HTTPException as e:
        raise e

@app.route("/pokemon", methods=["GET"])
def pokemon() -> Any:
    name: Optional[Any] = request.args.get('name')
    try:
        pokemon: Dict[str, Any] = get_pokemon(name)
        return jsonify(pokemon)
    except HTTPException as e:
        raise e

@app.route("/quote", methods=["GET"])
def quote() -> Any:
    try:
        quote = get_quote()
        return jsonify(quote)
    except HTTPException as e:
        raise e

@app.route("/chuck", methods=["GET"])
def chuck_joke() -> Any:
    try:
        quote = get_chuck_joke()
        return jsonify(quote)
    except HTTPException as e:
        raise e

@app.route('/download', methods=["GET"])
def download_by_id() -> Any:
    try:
        url: Optional[Any] = request.args.get('url')
        binary, title = download_video(url)
        return Response(binary, headers={'Content-Disposition': 'attachment; '
                                        'filename=' + f"{title}.mp4"})
    except HTTPException as e:
        raise e

def errorhandler(e: HTTPException) -> Any:
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return jsonify(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run()