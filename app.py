from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import threading, time, requests

load_dotenv()

app = Flask(__name__)
api = Api(app)


def autocall_main_api():
    time.sleep(2)
    try:
        requests.get("http://127.0.0.1:3387/main")
    except Exception as e:
        print("Startup call failed to main API!")

from routes import *

if __name__ == '__main__':
    threading.Thread(target=autocall_main_api, daemon=True).start()
    app.run(port=3387, debug=False, host='0.0.0.0')