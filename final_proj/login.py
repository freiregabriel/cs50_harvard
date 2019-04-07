from flask import session, redirect, Blueprint, request, render_template


from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash


from .exceptions import InvalidUsage
from .database import db


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


login_blueprint = Blueprint('login_blueprint', __name__, template_folder='templates')


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login_page():
    """ Log user in """
    # forget user id
    session.clear()
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('error.html', error_name='Invalid credentials.', error_desc='Invalid credentials.', error_code=403)
        
        # check database username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=username)

        # ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return render_template('error.html', error_name="invalid username and/or password", error_desc="invalid username and/or password", error_code=403)
        
        # add user to session
        session["user_id"] = rows[0]["id"]

        # redirect
        return redirect('/')

    # render login template
    return render_template('login.html')


@login_blueprint.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
