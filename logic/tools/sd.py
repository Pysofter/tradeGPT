from colorama import Fore, Style, init

init(autoreset=True)

def draw_summary_candles(data: object) -> str:
    total_candles = len(data)
    green_count = 0
    red_count = 0

    # Подсчет бычьих и медвежьих свечей
    for candle in data:
        if float(candle['close']) > float(candle['open']):
            green_count += 1
        else:
            red_count += 1

    # Вычисляем проценты
    green_percentage = (green_count / total_candles) * 100 if total_candles > 0 else 0
    red_percentage = (red_count / total_candles) * 100 if total_candles > 0 else 0

    # Определяем максимальную высоту свечи
    max_height = 50

    # Нормализация
    green_candle_height = int((green_count / total_candles) * max_height)
    red_candle_height = int((red_count / total_candles) * max_height)

    # Отображение зеленой свечи
    green_body = '█' * green_candle_height
    print(f"{Fore.GREEN}Long Candle : {green_body} {Style.RESET_ALL}")

    # Отображение красной свечи
    red_body = '█' * red_candle_height
    print(f"{Fore.RED}Short Candle: {red_body} {Style.RESET_ALL}")

    return f"(Long: {green_count} | {green_percentage:.2f}%) (Short: {red_count} | {red_percentage:.2f}%) -> 7d"