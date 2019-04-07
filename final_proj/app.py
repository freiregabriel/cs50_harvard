
from flask import Flask, render_template, redirect, request, jsonify, Response, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from datetime import datetime
from typing import Any, Optional, Dict, Union


# exceptions
from .exceptions import NoPokemonNameError, InvalidPokemonNameError, NoQuoteError, YoutubeError, InvalidUsage


# utilities
from .pokemon import pokemon_blueprint
from .quote import quotes_blueprint
from .chuck import chuck_blueprint
from .youtube import youtube_blueprint
from .hackernews import hackernews_blueprint
from .login import login_blueprint
from .register import registration_blueprint


# Settings
from .settings import VERSION
from .database import create_tables


app = Flask(__name__)


# create database tables if they don't exist
create_tables()


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
def after_request(response:Any) -> Response:
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# register blueprints
app.register_blueprint(pokemon_blueprint)
app.register_blueprint(hackernews_blueprint)
app.register_blueprint(chuck_blueprint)
app.register_blueprint(quotes_blueprint)
app.register_blueprint(youtube_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(registration_blueprint)


# Error handling
def apology(e: HTTPException) -> Response:
    """ handle error as JSON or Template """
    response = jsonify({
        "name": e.name,
        "description": e.description,
        "code": e.code
    })
    response.status_code = e.code
    return response


def _render_with_version(templateUrl: str):
    """ reusable function to render template aways passing the current application version """
    return render_template(templateUrl, version=version, session=session)


# Pages
@app.route("/")
def index() -> Any:
    """ Show portfolio of stocks """
    return _render_with_version("index.html")


@app.route("/dogs")
def dogs() -> Any:
    """ dogs page """
    return _render_with_version("dogs.html")


@app.route("/cats")
def cats() -> Any:
    """ cats page """
    return _render_with_version("cats.html")


@app.route("/country_finder_by_ip")
def ip() -> Any:
    """ ip page """
    return _render_with_version("ip.html")


@app.errorhandler(HTTPException)
def errorhandler(e: HTTPException) -> Any:
    """ Handle error """
    print(e)
    if not isinstance(e, HTTPException):
        e = InternalServerError()

    return apology(e)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
