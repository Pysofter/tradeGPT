import pandas as pd

def analyze_candlestick_patterns(candles):
    """
    Анализирует свечные данные и определяет бычьи или медвежьи паттерны.

    :param candles: Список свечей в формате словаря
    :return: Словарь с количеством бычьих и медвежьих паттернов
    """
    # Преобразование данных в DataFrame
    df = pd.DataFrame(candles)
    df['open'] = df['open'].astype(float)
    df['close'] = df['close'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)

    # Инициализация счетчиков паттернов
    bullish_patterns = 0
    bearish_patterns = 0
    call = 0
    report = None

    # Анализ паттернов
    for i in range(1, len(df)):
        # Проверка на бычий паттерн
        if df['close'].iloc[i] > df['open'].iloc[i]: # Текущая свеча бычья
            if df['close'].iloc[i-1] < df['open'].iloc[i-1]: # Предыдущая свеча медвежья
                bullish_patterns += 1 # Паттерн "бычьей engulfing"

        # Проверка на медвежий паттерн
        if df['close'].iloc[i] < df['open'].iloc[i]: # Текущая свеча медвежья
            if df['close'].iloc[i-1] > df['open'].iloc[i-1]: # Предыдущая свеча бычья
                bearish_patterns += 1 # Паттерн "медвежьей engulfing"
    
    if bullish_patterns > bearish_patterns:
        call = 3
        report = f"Бычьих паттернов: {bullish_patterns}, Медвежьих паттернов: {bearish_patterns} -> LONG"
    elif bearish_patterns > bullish_patterns:
        call = 1
        report = f"Бычьих паттернов: {bullish_patterns}, Медвежьих паттернов: {bearish_patterns} -> SHORT"
    else:
        call = 2
        report = f"Бычьих паттернов: {bullish_patterns}, Медвежьих паттернов: {bearish_patterns} -> NEUTRAL"

    return {
        'call': call,
        'report': report
    }
