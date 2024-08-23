from typing import List, Optional

from eshop.businsess_logic.order import Order

_orders: List[Order] = []


def save(order: Order):
    for i in range(len(_orders)):
        existed_order = _orders[i]
        if existed_order.id == order.id:
            _orders[i] = order
            break
    else:
        _orders.append(order)


def get_by_id(id: str) -> Optional[Order]:
    return next((o for o in _orders if o.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return _orders[start:end]
