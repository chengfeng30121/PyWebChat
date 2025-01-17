from flask import *
import webview
import platform
import requests

def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()
    return response['ip']

app = Flask(__name__, template_folder="assets")
@app.route('/')
def index():
    print("get a request")
    with open('assets/index.html', 'r') as f:
        return f.read().replace("%SYSTEM%", platform.system()).replace("%IP%", get_ip())

if __name__ == '__main__':
    webview.create_window('Arch Test', url=app, min_size=(600, 450))
    webview.start(ssl=True)