from logic.data.data import demo
from logic.tools.calc import calc
from logic.tools.fibo import fibo
from logic.tools.liquidity import define_liquidity_zones
from logic.tools.pattern import analyze_candlestick_patterns
from logic.tools.sd import draw_summary_candles
from logic.data.quote import demo_quote
from .stats import analyze_order_book

trend = None
tp = None
sl = None
report = None

class Trade():

    @staticmethod
    def analyze(token: str) -> object:
        json_data = demo_quote(token)

        price_data = [float(item['close']) for item in json_data["data"]]
        volume_data = [float(item['volume']) for item in json_data["data"]]

        liquidity_zones, price_trend, call = define_liquidity_zones(price_data, volume_data)
        currency = demo(token)
        orders = analyze_order_book(token)
        trends = analyze_candlestick_patterns(json_data['data'])['call']
        tc = calc(float(currency['data']['highPrice']), float(currency['data']['lowPrice']), float(currency['data']['lastPrice']))
        tfibo = fibo(float(currency['data']['highPrice']), float(currency['data']['lowPrice']), float(currency['data']['lastPrice']))

        if (int(tc) == 3 and int(tfibo) == 3 and orders == 3 and call == 3 and trends == 3):
            trend = f'{token} -> LONG'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал:\n[+] {token} -> LONG, сейчас хорошая точка входа для лонг позиций'
        elif ((int(tc) == 3 or int(tc == 2)) and (int(tfibo) == 3 or int(tfibo) == 2) and orders == 3 and call == 3 and trends == 3):
            trend = f'{token} -> LONG'
            tp = f'10-15%'
            sl = f'15%'
            report = f'По вашему запросу анализ показал:\n[+] {token} -> LONG, сейчас хорошая точка входа для лонг позиций'
        elif ((int(tc) == 3 or int(tc == 1)) and (int(tfibo) == 3 or int(tfibo) == 1) and orders == 3 and call == 3 and trends == 3):
            trend = f'{token} -> LONG'
            tp = f'5-12%'
            sl = f'10%'
            report = f'По вашему запросу анализ показал:\n[+] {token} -> LONG, сейчас хорошая точка входа для лонг позиций'
        elif (int(tc) == 1 and int(tfibo) == 1 and orders == 1 and call == 1 and trends == 1):
            trend = f'{token} -> SHORT'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал:\n[-] {token} -> SHORT, сейчас хорошая точка входа для шорт позиций'
        elif ((int(tc) == 1 or int(tc) == 2) and (int(tfibo) == 2 or int(tfibo) == 1) and orders == 1 and call == 1 and trends == 1):
            trend = f'{token} -> SHORT'
            tp = f'15-15%'
            sl = f'15%'
            report = f'По вашему запросу анализ показал:\n[-] {token} -> SHORT, сейчас хорошая точка входа для шорт позиций'
        elif ((int(tc) == 1 or int(tc) == 3) and (int(tfibo) == 1 or int(tfibo) == 3) and orders == 1 and call == 1 and trends == 1):
            trend = f'{token} -> SHORT'
            tp = f'5-12%'
            sl = f'10%'
            report = f'По вашему запросу анализ показал:\n[-] {token} -> SHORT, сейчас хорошая точка входа для шорт позиций'
        else:
            trend = f'{token} -> NEUTRAL'
            report = f'По вашему запросу анализ показал:\n[?] {token} -> NEUTRAl, сейчас непонятная ситуация, не рискуйте своими средствами!'
            tp = '-'
            sl = '-'

        data = {
            'analyze': {
                'trend': tc,
                'fibo': tfibo,
                'trend': trend,
                'orders': orders,
                'sl': sl,
                'tp': tp,
                'report': report
            }
        }
        return data
    
    @staticmethod
    def fibo_analyze(token: str) -> object:
        currency = demo(token)
        tfibo = fibo(float(currency['data']['highPrice']), float(currency['data']['lowPrice']), float(currency['data']['lastPrice']))

        if (int(tfibo) == 3):
            trend = f'{token} -> LONG'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал (FIBO):\n[+] {token} -> LONG, сейчас хорошая точка входа для лонг позиций' 
        elif (int(tfibo) == 2):
            trend = f'{token} -> NEUTRAL'
            tp = f'5-12%'
            sl = f'10%'
            report = f'По вашему запросу анализ показал (FIBO):\n[?] {token} -> NEUTRAL'
        elif (int(tfibo) == 1):
            trend = f'{token} -> SHORT'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал (FIBO):\n[-] {token} -> SHORT, сейчас хорошая точка входа для шорт позиций'

        data = {
            'analyze': {
                'fibo': tfibo,
                'trend': trend,
                'sl': sl,
                'tp': tp,
                'report': report
            }
        }
        return data
    
    @staticmethod
    def calc_analyze(token: str) -> object:
        currency = demo(token)
        tc = calc(float(currency['data']['highPrice']), float(currency['data']['lowPrice']), float(currency['data']['lastPrice']))

        if (int(tc) == 3):
            trend = f'{token} -> LONG'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал (CALC):\n[+] {token} -> LONG, сейчас хорошая точка входа для лонг позиций' 
        elif (int(tc) == 2):
            trend = f'{token} -> NEUTRAL'
            tp = f'5-12%'
            sl = f'10%'
            report = f'По вашему запросу анализ показал (CALC):\n[?] {token} -> NEUTRAL'
        elif (int(tc) == 1):
            trend = f'{token} -> SHORT'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал (CALC):\n[-] {token} -> SHORT, сейчас хорошая точка входа для шорт позиций'

        data = {
            'analyze': {
                'trend': trend,
                'sl': sl,
                'tp': tp,
                'report': report
            }
        }
        return data

    @staticmethod
    def sad_analyze(token: str) -> object:
        orders = analyze_order_book(token)

        if (int(orders) == 3):
            trend = f'{token} -> LONG'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал (S&D):\n[+] {token} -> LONG, сейчас хорошая точка входа для лонг позиций' 
        elif (int(orders) == 2):
            trend = f'{token} -> NEUTRAL'
            tp = f'5-12%'
            sl = f'10%'
            report = f'По вашему запросу анализ показал (S&D):\n[?] {token} -> NEUTRAL'
        elif (int(orders) == 1):
            trend = f'{token} -> SHORT'
            tp = f'15-30%'
            sl = f'35%'
            report = f'По вашему запросу анализ показал (S&D):\n[-] {token} -> SHORT, сейчас хорошая точка входа для шорт позиций'

        data = {
            'analyze': {
                'trend': trend,
                'sl': sl,
                'tp': tp,
                'report': report
            }
        }
        return data

    @staticmethod
    def liquidity_analyze(token: str) -> object:
        json_data = demo_quote(token)

        price_data = [float(item['close']) for item in json_data["data"]]
        volume_data = [float(item['volume']) for item in json_data["data"]]

        liquidity_zones, price_trend, call = define_liquidity_zones(price_data, volume_data)

        data = {
            'analyze': {
                'call': f'{call}',
                'report': f'{liquidity_zones}\n{price_trend}'
            }
        }
        return data
    
    @staticmethod
    def sd_analyze(token: str) -> None:
        json_data = demo_quote(token)['data']
        return draw_summary_candles(json_data)
    
    @staticmethod
    def pattern_analyze(token: str) -> None:
        json_data = demo_quote(token)
        return analyze_candlestick_patterns(json_data['data'])['report']