from flask import Flask, request, render_template, jsonify

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
        with open("answers.txt", "a", encoding='utf-8') as file:  # Открываем файл в режиме добавления
            file.write(f"{answer},{message}\n")  # Сохраняем ответ с новой строки
        return jsonify({"message": "Ответ сохранен!"}), 200
    return render_template('index.html')  # Указываем файл index.html

if __name__ == '__main__':
    app.run(debug=True)
