import time
import requests
import hmac
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo(currency):
    payload = {}
    path = '/openApi/swap/v2/quote/ticker'
    method = "GET"
    paramsMap = {
        "symbol": f"{currency}-USDT",
        "timestamp": str(int(time.time() * 1000))
    }
    paramsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    return signature

def send_request(method, path, urlpa, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlpa, get_sign(SECRETKEY, urlpa))
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.json()

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
    return paramsStr + "&timestamp=" + str(int(time.time() * 1000)) if paramsStr else "timestamp=" + str(int(time.time() * 1000))
