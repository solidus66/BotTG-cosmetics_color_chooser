import os
import time
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive"


def run():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


def keep_alive():
    url = "https://bottg-cosmetics-color-chooser.onrender.com"

    while True:
        try:
            requests.get(url)
            print(f"Sent keep-alive request to {url}")
        except Exception as e:
            print(f"Error keeping alive: {e}")
        time.sleep(600)