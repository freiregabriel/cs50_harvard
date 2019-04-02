from flask import session, redirect, Blueprint, request, render_template
from .exceptions import InvalidUsage
from werkzeug.security import check_password_hash, generate_password_hash
from .database import db


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
                raise InvalidUsage("Must provide username/password", 400)
            if password_again != password:
                raise InvalidUsage("Passwords are different", 400)

            # generate hash
            hash_ = generate_password_hash(password)

            # Query database to create a new user row
            result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash_)",
                    username=username, hash_=hash_)
            
            # validate registration
            if not result:
                raise InvalidUsage("Username already taken", 400)
            
            # login
            session['user_id'] = result
            
            # redirect
            return redirect("/")
    except (TypeError, Exception, HTTPException, InvalidUsage) as e:
        return redirect('/')
    
    return render_template("register.html")