#TradixGPT - v0.1
import time, random
from colorama import init, Fore
from logic.trade import Trade
from logic.data.wiki import wiki
import json
import os

cases = ['btc', 'eth', 'sol', 'bnb', 'atom', 'uni', 'trx', 'doge', 'toncoin', 'inj', 'wif', 'not', 'strk', 'avax', 'op', 'etc', 'notcoin', 'comp', 'sui', 'near', 'bch', 'tia', 'people', 'dydx', 'arb', 'fil', 'apt', 'ada', 'dogs', 'ldo', 'aave', 'reef', 'kas', 'pol']
tools = ['fibo', 'calc', 'sad', 'liq', '7d', 'pattern']

class Chatbot:
    def __init__(self, filename):
        self.filename = filename
        self.responses = self.load_responses()

    def load_responses(self):
        """Загрузка ответов из JSON файла, создание файла, если он отсутствует."""
        if not os.path.exists(self.filename):
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
        tool = [tl for tl in tools if tl in user_input]
        if key:
            if tool:
                if 'fibo' in tool:
                    return [Trade.fibo_analyze(key[0].upper())['analyze']['report']]
                elif 'calc' in tool:
                    return [Trade.calc_analyze(key[0].upper())['analyze']['report']]
                elif 'liq' in tool:
                    return [Trade.liquidity_analyze(key[0].upper())['analyze']['report']]
                elif '7d' in tool:
                    return [Trade.sd_analyze(key[0].upper())]
                elif 'pattern' in tool:
                    return [Trade.pattern_analyze(key[0].upper())]
                else:
                    return [Trade.sad_analyze(key[0].upper())['analyze']['report']]
            else:
                return [Trade.analyze(key[0].upper())['analyze']['report']]
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
            user_input = input(Fore.CYAN + "Вы: ").strip().lower()
            if user_input == "выход":
                print("Чат-бот завершён.")
                break

            response = self.respond(user_input)
            if response:
                time.sleep(0.5)
                try:
                    words = response["words"]
                except:
                    words = response
                print(Fore.GREEN + f"ИИ: {random.choice(words)}")
            else:
                print(Fore.GREEN + f'ИИ: Информация из открытых источников: {wiki(user_input)}')
                #new_response = input("Пожалуйста, дайте ответ на это (или введите '-'): ").strip()
                #if new_response.lower() == "-":
                    #print("Отмена добавления ответа.")
                #else:
                    #self.add_response(user_input, [new_response])

if __name__ == "__main__":
    try:
        responses_file = './cache/responses.json'
        context_file = './cache/context.json'
        chatbot = Chatbot(responses_file)
        chatbot.run()
    except:
        print("Чат-бот завершён.")
