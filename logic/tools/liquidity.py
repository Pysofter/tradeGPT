import pandas as pd
import numpy as np

def define_liquidity_zones(price_data, volume_data, price_threshold=0.01, volume_threshold=1000):
    """
    Определяет зоны ликвидности на основе ценовых и объемных данных, а также возможное движение цены.

    :param price_data: Список или массив цен
    :param volume_data: Список или массив объемов
    :param price_threshold: Ширина диапазона вокруг уровня цены для определения зоны ликвидности
    :param volume_threshold: Минимальный объем для определения значимости зоны ликвидности
    :return: DataFrame с уровнями цен и соответствующими объемами и направление движения цены
    """
    # Создание DataFrame для анализа
    df = pd.DataFrame({'Price': price_data, 'Volume': volume_data})

    # Округляем цены до ближайшего значения с заданным шагом
    df['Price_Rounded'] = df['Price'].round(-int(np.log10(price_threshold)))

    # Группировка по округленным ценовым уровням
    volume_groups = df.groupby('Price_Rounded')['Volume'].sum().reset_index()

    # Фильтрация зон ликвидности по объему
    liquidity_zones = volume_groups[volume_groups['Volume'] >= volume_threshold]

    # Сортировка зон ликвидности по объему в порядке убывания
    liquidity_zones = liquidity_zones.sort_values(by='Volume', ascending=False).reset_index(drop=True)

    # Определение зоны поддержки (наибольший объем на низких ценах) и снятия ликвидности (на высоких ценах)
    support_zone = liquidity_zones.iloc[-1] # Самая низкая зона (поддержка)
    liquidity_grab_zone = liquidity_zones.iloc[0] # Самая высокая зона (снятие ликвидности)

    # Текущая цена — это последняя цена из price_data
    current_price = price_data[-1]

    # Определение направления движения цены
    if current_price < support_zone['Price_Rounded']:
        price_trend = f"Цена вероятно пойдет вверх к зоне поддержки."
        call = 3
    elif current_price > liquidity_grab_zone['Price_Rounded']:
        price_trend = f"Цена вероятно пойдет вниз к зоне снятия ликвидности."
        call = 1
    else:
        price_trend = "Нет явных сигналов для движения цены."
        call = 0

    return liquidity_zones, price_trend, call