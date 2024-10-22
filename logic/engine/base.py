import json
import os
from ..trade import Buy

cases = ['btc', 'eth', 'sol', 'bnb', 'atom', 'uni', 'trx', 'doge', 'toncoin', 'inj', 'wif', 'not', 'strk', 'avac', 'op']

class Chatbot:
    def __init__(self, filename):
        self.filename = filename
        self.responses = self.load_responses()

    def load_responses(self):
        """Загрузка ответов из JSON файла, создание файла, если он отсутствует."""
        if not os.path.exists(self.filename):
            # Create an empty dictionary and save it as a JSON file if it doesn't exist
            self.save_responses({})
            return {}

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Ошибка чтения файла. Проверьте формат JSON.")
            return {}

    def save_responses(self, responses=None):
        """Сохранение ответов в JSON файл."""
        if responses is not None:
            self.responses = responses
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.responses, file, ensure_ascii=False, indent=4)

    def respond(self, user_input):
        """Генерация ответа на основе ввода пользователя."""
        user_input = user_input.strip().lower()
        key = [cs for cs in cases if cs in user_input]
        if key:
            return key[0]
        else:
            return self.responses.get(user_input)

    def add_response(self, user_input, new_response):
        """Добавление нового ответа для незнакомого ввода."""
        user_input = user_input.strip().lower()
        self.responses[user_input] = new_response
        self.save_responses()
        print(f"Ответ '{new_response}' добавлен для '{user_input}'.")

    def run(self):
        """Основной цикл работы чат-бота."""
        print("TradixGPT запущен. Для выхода введите 'выход'.")
        while True:
            user_input = input("Вы: ").strip().lower()
            if user_input == "выход":
                print("Чат-бот завершён.")
                break
            
            response = self.respond(user_input)
            if response:
                print(f"ИИ: {response}")
            else:
                print("ИИ: Я не знаю, как ответить на это, пиши по теме")
                new_response = input("Пожалуйста, дайте ответ на это (или введите 'отмена'): ").strip()
                if new_response.lower() == "отмена":
                    print("Отмена добавления ответа.")
                else:
                    self.add_response(user_input, new_response)

# Файл для хранения ответов
responses_file = 'responses.json'
chatbot = Chatbot(responses_file)
chatbot.run()
