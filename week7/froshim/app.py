from flask import Flask, render_template, request, redirect, jsonify
import time
import numba
import pandas as pd
from numba.decorators import jit

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
    

class CSVManager:
    def __init__(self, filename):
        self.filename = filename

    @jit
    def append_obj(self, obj: object):
        df = pd.read_csv(self.filename)
        df = df.append(obj, ignore_index=True)
        df.to_csv(self.filename, index=False)
    @jit
    def make_list(self) -> list:
        df = pd.read_csv(self.filename)
        nparr = df.values
        return nparr.tolist()


csv_manager = CSVManager('registered.csv')


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/registrants')
def registrants():
    return render_template('registrants.html')


@app.route('/registrants_json')
def registrants_json():
    lst = csv_manager.make_list()
    return jsonify(lst)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not dorm or not name:
        return render_template("error.html")

    csv_manager.append_obj( { 'name': name, 'dorm': dorm } )
    return redirect("/registrants")



# def send_email(email, message):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("gabrielfreiredev@gmail.com", os.getenv("EMAIL_PASSWORD"))
#     server.sendmail("gabrielfreiredev@gmail.com", email, message)


# def add_to_csv(obj):
    # with open("registered.csv", "a") as f:
    #     writer = csv.writer(f)
    #     writer.writerow((name, dorm))


# def filter_list(l):
#     return [item for item in l if len(item) > 0]


# def get_from_csv(file_name):
    # with open(file_name, "r") as f:
    #     reader = csv.reader(f)
    #     tmp_students = list(reader)
    #     students = filter_list(tmp_students)
    #     return students


if __name__ == "__main__":
    app.run()