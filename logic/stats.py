from logic.data.order import demo
import json

def analyze_order_book(token: str) -> int:

    response = demo(token)
    order_book = json.loads(response)

    order_data = order_book.get("data", {})
    
    bids = order_data.get("bids", [])
    asks = order_data.get("asks", [])

    bids_total = sum(float(bid[0]) * float(bid[1]) for bid in bids)
    asks_total = sum(float(ask[0]) * float(ask[1]) for ask in asks)


    if bids_total > asks_total:
        return 3
    elif bids_total < asks_total:
        return 1
    else:
        return 2
