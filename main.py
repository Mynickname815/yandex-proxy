from flask import Flask, jsonify
import requests

app = Flask(__name__)  # ← это ключевая строка

TOKEN = 'y0__xCW0ZeZBhjMsjkgsJSygRQsHbmjxmG5hOtYTyVo7MquBuZMSQ'
FORM_ID = '688b30d6f47e730eb47fc9da'

@app.route('/')
def index():
    return 'Yandex Forms Proxy is running.'

@app.route('/form')
def get_form_data():
    url = f'https://api.forms.yandex.ru/v1/forms/{FORM_ID}/responses'
    headers = {'Authorization': f'OAuth {TOKEN}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({'error': response.status_code, 'text': response.text}), 500
