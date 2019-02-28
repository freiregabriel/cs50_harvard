from flask import Flask, session, render_template, request
from sql_lib import SQL
app = Flask(__name__)

db = SQL('sqlite:///app.db')

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["MEMORIOUS_DEBUG"] = True
# Create session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def index():
    q = request.args.get('q')
    rows = []
    if q:
        rows = db.execute(f'SELECT * FROM registrants WHERE name = :q', q=q) # NOT vulnerable to SQL Injection attack
        # c.execute(f'SELECT * FROM registrants WHERE name = {q}') # vulnerable to SQL Injection attack
    else:
        rows = db.execute('SELECT * FROM registrants')
    return render_template("index.html", rows=rows)

# session['item'] = 'item' < how to set a session value
if __name__ == "__main__":
    app.run()