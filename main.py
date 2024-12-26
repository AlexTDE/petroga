from flask import Flask, request, render_template, jsonify
import requests

BOT_TOKEN = '7169416179:AAHdY_lwlNpGkQyCL8xj7WJIh_rgUqfOlUw'
CHAT_ID = '-1002056665555'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем выбранный ответ из формы
        answer = request.form.get("answer")
        if not answer:
            return jsonify({"error": "Нет ответа"}), 400
        message = request.form.get('message')
        # Сохраняем ответ в файл
        # Отправка сообщения в Telegram
        text = f"Option: {answer}\nСообщение: {message}"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
            "chat_id": CHAT_ID,
            "text": text
        })
        return jsonify({"message": "Ответ сохранен!"}), 200
    return render_template('index.html')  # Указываем файл index.html

if __name__ == '__main__':
    app.run(debug=True)
