import pandas as pd
import numpy as np

def detect_pump_dump(price_data, volume_data, rsi_threshold=70, volatility_threshold=1.5, volume_increase_factor=2):
    """
    Определяет вероятность пампа или дампа на основе ценовых и объемных данных.

    :param price_data: Список или массив цен
    :param volume_data: Список или массив объемов
    :param rsi_threshold: Порог RSI для определения перекупленности
    :param volatility_threshold: Порог волатильности для определения резких движений
    :param volume_increase_factor: Множитель для определения роста объема
    :return: Строка с результатом анализа
    """
    # Конвертируем цены и объемы в DataFrame
    df = pd.DataFrame({'Price': price_data, 'Volume': volume_data})

    # Рассчитываем логарифмы цен для вычисления роста
    df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))
    df['Volatility'] = df['Log_Return'].rolling(window=20).std() * np.sqrt(20) # Годовая волатильность

    # Индикатор RSI
    delta = df['Price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Условия для определения пампа или дампа
    last_volume = df['Volume'].iloc[-1]
    previous_volume = df['Volume'].iloc[-2]
    current_volatility = df['Volatility'].iloc[-1]

    if df['RSI'].iloc[-1] > rsi_threshold:
        return "Вероятен дамп: рынок переоценен (RSI выше порога)."
    elif current_volatility > volatility_threshold and (last_volume / previous_volume) > volume_increase_factor:
        return "Вероятен памп: резкое увеличение объема и волатильности."
    elif df['RSI'].iloc[-1] < (100 - rsi_threshold):
        return "Вероятен памп: рынок недооценен."
    else:
        return "Нет явных сигналов о пампе или дампе."

# Пример использования
price_data = [100, 101, 102, 105, 110, 95, 90, 92, 88, 121]
volume_data = [1000, 1200, 1500, 2000, 2500, 1800, 2000, 3000, 5000, 8000]

result = detect_pump_dump(price_data, volume_data)
print(result)