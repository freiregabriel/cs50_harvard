from flask import session, redirect, Blueprint, request, render_template
from werkzeug.security import check_password_hash, generate_password_hash

from .database import db
from .exceptions import InvalidUsage


registration_blueprint = Blueprint('registration_blueprint', __name__, template_folder='templates')


@registration_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "POST":
            """Register user"""
            username = request.form.get("username")
            password = request.form.get("password")
            password_again = request.form.get("confirmation")

            # validate input
            if not username or not password or not password_again:
                return render_template('error.html', error_name="Must provide username/password", error_desc="Must provide username/password", error_code=400)
            if password_again != password:
                return render_template('error.html', error_name="Passwords are different", error_desc="Passwords are different", error_code=400)

            # generate hash
            hash_ = generate_password_hash(password)

            # Query database to create a new user row
            result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash_)",
                    username=username, hash_=hash_)
            
            # validate registration
            if not result:
                return render_template('error.html', error_name="Username already taken", error_desc="Username already taken", error_code=400)
            
            # login
            session['user_id'] = result
            
            # redirect
            return redirect("/")
    except InvalidUsage as e:
        if not isinstance(e, InvalidUsage):
            e = InvalidUsage(e.description, e.code)
        raise e
    except Exception as e:
        raise e

    return render_template("register.html")