def calc(high: float, low: float, current: float) -> int:
    """
    Determine the trend based on the current price's position within the high-low range.

    Args:
        high (float): The high price.
        low (float): The low price.
        current (float): The current price.

    Returns:
        int: Trend indicator (1 for downtrend, 2 for neutral, 3 for uptrend).
    """
    if high <= low:
        raise ValueError("High price must be greater than low price.")

    price_range = high - low
    if price_range == 0:
        return 2

    position_percentage = ((current - low) / price_range) * 100

    if position_percentage >= 70:
        return 3 
    elif position_percentage <= 30:
        return 1
    else:
        return 2
