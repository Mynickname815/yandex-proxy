from flask import Flask, jsonify
import requests

app = Flask(__name__)

TOKEN = 'y0__xCW0ZeZBhjMsjkgsJSygRQsHbmjxmG5hOtYTyVo7MquBuZMSQ'
FORM_ID = '688b30d6f47e730eb47fc9da'

@app.route('/')
def index():
    return 'Yandex Forms Proxy is running.'

@app.route('/form')
def get_form_data():
    try:
        url = f'https://api.forms.yandex.ru/v1/forms/{FORM_ID}/responses'
        headers = {'Authorization': f'OAuth {TOKEN}'}
        resp = requests.get(url, headers=headers)

        # Печатаем статус и тело ответа в консоль
        print(f"Yandex API status: {resp.status_code}")
        print(f"Yandex API body: {resp.text}")

        return (resp.text, resp.status_code, {'Content-Type': 'application/json'})

    except Exception as e:
        print(f"EXCEPTION: {e}")  # ← это будет видно в Render логах
        return jsonify({'error': 'internal', 'message': str(e)}), 500
