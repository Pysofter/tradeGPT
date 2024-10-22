from typing import Literal

FIBO_LEVELS = {
    'level_0': 0.0,
    'level_23.6': 0.236,
    'level_38.2': 0.382,
    'level_61.8': 0.618,
    'level_100': 1.0
}

def fibo(high: float, low: float, current: float) -> Literal[1, 2, 3]:
    """
    Determine the trend based on Fibonacci retracement levels.

    Args:
        high (float): The high price.
        low (float): The low price.
        current (float): The current price.

    Returns:
        int: Trend indicator (1, 2, or 3).
    """
    if high <= low:
        raise ValueError("High price must be greater than low price.")

    price_range = high - low
    levels = {
        'level_0': low + price_range * FIBO_LEVELS['level_0'],
        'level_23.6': low + price_range * FIBO_LEVELS['level_23.6'],
        'level_38.2': low + price_range * FIBO_LEVELS['level_38.2'],
        'level_61.8': low + price_range * FIBO_LEVELS['level_61.8'],
        'level_100': high
    }

    if current <= levels['level_38.2']:
        trend = 3
    elif current >= levels['level_61.8']:
        trend = 1
    else:
        trend = 2

    return trend
