from flask import Flask, render_template_string, request
from datetime import datetime
import pytz
from pytz import timezone
# print(pytz.all_timezones)
app = Flask(__name__)

def get_place_time(place, time):
    div = "<div>"
    end_div = "</div>"
    return f"{div}The current date and time in <strong>{place}</strong> is <strong>{time}</strong>{end_div}"

@app.route('/')
def time():
    title="Time App"
    now_america = datetime.now(timezone('America/New_York'))
    now_ireland = datetime.now(timezone('Europe/Dublin'))
    start = f"<html><head><title>Time</title></head><body><h1>{title}</h1>"
    end = "</body></html>"
    cambridge_time = get_place_time('Cambridge', now_america)
    irish_time = get_place_time('Ireland', now_ireland)
    return render_template_string(f"{start}{cambridge_time}{irish_time}{end}")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do one thing
    else:
        # do a different thing