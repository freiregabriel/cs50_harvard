import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # get data from csv file and render sheet.html
    data = _get_from_csv("survey.csv")
    return render_template("sheet.html", data=data)


@app.route("/form", methods=["POST"])
def post_form():
    # Get user input
    name = request.form.get("name")
    email = request.form.get("email")
    ai_w = request.form.get("ai_wish")
    # Validade
    if not email or not name or not ai_w:
        return render_template("error.html", message="E-mail, name and AI wish are mandatory")

    # Add to csv file and redirect to sheet page
    _add_to_csv(name, email, ai_w)
    return redirect("/sheet")


def _add_to_csv(name, email, ai_w):
    """ Add data to survey.csv file """
    with open("survey.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow((name, email, ai_w))


def _get_from_csv(file_name):
    """ Return a list of the data inside a csv file """
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        lst = list(reader)
        return lst