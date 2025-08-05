from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Убедись, что здесь твой реальный токен и ID формы
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

        # Отладка: выводим весь текст ошибки от Яндекса
        return (resp.text, resp.status_code, {'Content-Type': 'application/json'})

    except Exception as e:
        # Отладка: выводим конкретную ошибку Python
        return jsonify({'error': 'internal', 'message': str(e)}), 500
