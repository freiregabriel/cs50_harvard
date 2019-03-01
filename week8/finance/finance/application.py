import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

flash_message = ""
def get_flashed_messages():
    return flash_message

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # query database for user information and shares
    user_id = session["user_id"]
    user = db.execute('SELECT * FROM users WHERE id=:id', id=user_id)
    shares = db.execute('SELECT * FROM shares WHERE userid=:user_id', user_id=user_id)
    if not shares:
        shares = []
        
    return render_template("index.html", user=user[0], shares=shares)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # return apology("TODO")
    if request.method == 'POST':
        user_id = session['user_id']
        symbol = request.form.get('symbol')
        shares = request.form.get('shares')

        try:
            # check for integers
            shares = int(shares)
        except Exception as e:
            return apology("Invalid number of shares", 400)

        # validate input
        if not symbol or not shares:
            return apology("No symbol or share was defined", 400)

        # validate share number
        if shares <= 0:
            return apology("Invalid number of shares", 400)

        # get quote
        quote = lookup(symbol)

        if not quote:
            return apology("No quote was found", 400)

        user = db.execute('SELECT * FROM users WHERE id=:id', id=user_id)
        user_cash = user[0]['cash']

        # cost of the share(s)
        cost = quote['price'] * shares

        # check if the user can afford the share
        if user_cash > cost:
            rows = db.execute('SELECT * FROM shares WHERE symbol=:symbol AND userid=:id', symbol=symbol, id=user_id)

            # Save history
            db.execute('INSERT INTO history (symbol, shares, price, transacted, userid) VALUES (:symbol, :shares, :price, :transacted, :userid)',
                    symbol=symbol,shares=shares,price=quote['price'],transacted=datetime.datetime.now(), userid=user_id)

            if len(rows) != 1:
                # Create a new share with symbol
                db.execute('INSERT INTO shares (name, price, symbol, shares, userid, total_c) VALUES (:quote_name, :quote_price, :quote_symbol, :shares, :user_id, :total)',
                        quote_name=quote['name'], quote_price=quote['price'], quote_symbol=quote['symbol'], shares=shares, user_id=user_id, total=shares * quote['price'])
            else:
                # Update the share in case it already exists
                shares += rows[0]['shares']
                # calculate total
                total = rows[0]['total_c']
                total += (quote['price'] * shares)
                db.execute('UPDATE shares SET shares=:shares, price=:price, total_c=:total WHERE symbol=:symbol AND userid=:user_id',
                        shares=shares, price=quote['price'], total=total, symbol=symbol, user_id=user_id)

            # Update the user cash amount
            user_cash -= cost

            # Query database to update the user with new cash value
            db.execute('UPDATE users SET cash=:cash WHERE id=:id', cash=user_cash, id=user_id)
            return redirect("/")

        return apology("You don't have enough money", 403)

    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args.get('username')
    # check if username was already taken
    rows = db.execute("SELECT * FROM users WHERE username=:username", username=username)
    res = False
    if len(rows) == 0:
        res = True
    return jsonify(res)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # get users history
    histories = db.execute("SELECT * FROM history WHERE userid=:user_id", user_id=session['user_id'])
    return render_template("history.html", histories=histories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        if not symbol:
            return apology("No symbol was defined", 400)
        quote = lookup(symbol)
        if not quote:
            return apology("No quote found with this symbol", 400)
        return render_template("quote_result.html", quote=quote)

    return render_template("quote.html")


@app.route("/addcash", methods=['POST'])
@login_required
def add_cash():
    cash = request.form.get('cash')
    # validate input
    if not cash:
        return apology("No cash found", 400)
    
    # validate input type
    try:
        cash = float(cash)
    except Exception as e:
        return apology("Invalid amount", 400)
    
    # get user from database
    user = db.execute('SELECT * FROM users WHERE id=:id', id=session['user_id'])
    
    # update cash
    new_cash = user[0]['cash'] + cash
    
    # update user in the database
    db.execute('UPDATE users SET cash=:cash WHERE id=:id', cash=new_cash, id=session['user_id'])
    return redirect('/')
    

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """Register user"""
        username = request.form.get("username")
        password = request.form.get("password")
        password_again = request.form.get("confirmation")

        # validate input
        if not username or not password or not password_again:
            return apology("must provide username/password", 400)
        if password_again != password:
            return apology("passwords are different", 400)

        # generate hash
        hash_ = generate_password_hash(password)

        # generate initial cash
        cash = 10000
        
        # Query database to create a new user row
        result = db.execute("INSERT INTO users (username, hash, cash) VALUES (:username, :hash_, :cash)",
                username=username, hash_=hash_, cash=cash)
        if not result:
            return apology("Username already taken", 400)
        session['user_id'] = result
        flash_message = "Registered!"
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session['user_id']
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        shares = request.form.get('shares')

        try:
            shares = int(shares)
        except Exception as e:
            return apology("Invalid number of shares", 400)

        if shares <= 0:
            return apology("Invalid number of shares", 400)

        # validate input
        if not symbol or not shares:
            return apology("You must select the share and the amount", 400)

        # Query database for the shares
        rows = db.execute('SELECT * FROM shares WHERE symbol=:symbol AND userid=:user_id', symbol=symbol, user_id=user_id)
        share_row = rows[0]

        # check if there are sufficient shares
        if shares > share_row['shares']:
            return apology(f"You have {share_row['shares']} shares but want to sell {shares}", 400)

        # get current quote for updated price
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid share", 400)
        share_price = quote['price']

        # Query database for current user
        user = db.execute('SELECT * FROM users WHERE id=:id', id=user_id)

        # calculate sell price
        money = share_price * shares

        # calculate cash after sell
        user_cash = user[0]['cash']
        user_cash += money

        # calculate total
        total = rows[0]['total_c']
        total -= money

        # calculate new share amount
        new_share_amount = share_row['shares'] - shares

        # insert transaction to history table
        db.execute('INSERT INTO history (symbol, shares, price, transacted, userid) VALUES (:symbol, :shares, :price, :transacted, :userid)',
                symbol=symbol,shares=-shares,price=share_price,transacted=datetime.datetime.now(), userid=user_id)

        # update user with new cash
        db.execute('UPDATE users SET cash=:cash WHERE id=:id', cash=user_cash, id=user_id)

        # if there is no shares left, remove row from database
        if new_share_amount == 0:
            db.execute("DELETE FROM shares WHERE id=:id", id=share_row['id'])
        else:
            # just update row in case there are shares left
            db.execute('UPDATE shares SET shares=:shares, price=:price, total_c=:total WHERE symbol=:symbol AND userid=:user_id',
                    shares=new_share_amount, price=share_price, total=total, symbol=symbol, user_id=user_id)
        return redirect("/")

    symbols = db.execute("SELECT symbol FROM shares WHERE userid=:user_id", user_id=user_id)
    return render_template("sell.html", symbols=symbols)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == '__main__':
    app.run()