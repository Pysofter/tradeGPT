import time
import requests
import hmac
from hashlib import sha256
import json

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo_quote(currency):
    path = '/openApi/swap/v3/quote/klines'
    method = "GET"

    current_time = int(time.time() * 1000)
    start_time = (current_time - (7 * 24 * 3600 * 1000))

    paramsMap = {
        "symbol": f"{currency}-USDT",
        "interval": "4h",
        "limit": "30",
        "startTime": str(start_time)
    }
    
    paramsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr)

def get_sign(api_secret, payload):
    """Создает подпись HMAC для запроса."""
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    return signature

def send_request(method, path, urlpa):
    """Отправляет запрос к API с подписью и возвращает результат."""
    try:
        url = f"{APIURL}{path}?{urlpa}&signature={get_sign(SECRETKEY, urlpa)}"
        #print(f"Request URL: {url}")
        
        headers = {
            'X-BX-APIKEY': APIKEY,
        }

        response = requests.request(method, url, headers=headers)
        
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

def parseParam(paramsMap):
    """Сортирует параметры и добавляет метку времени."""
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join([f"{key}={paramsMap[key]}" for key in sortedKeys])
    return f"{paramsStr}&timestamp={int(time.time() * 1000)}"