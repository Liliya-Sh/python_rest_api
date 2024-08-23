from typing import List, Optional

from eshop.businsess_logic.product import Product

_products: List[Product] = [
    Product(
        id='1',
        name='Телевизор',
        price=15,
    ),
    Product(
        id='2',
        name='Кофемашина',
        price=10,
    ),
    Product(
        id='3',
        name='Ноутбук',
        price=12,
    )
]


def save(product: Product):
    # Проверяем, есть ли уже продукт c таким id
    for i in range(len(_products)):
        existed_product = _products[i]
        if existed_product.id == product.id:
            _products[i] = product
            break
    else:
        _products.append(product)


def delete_by_id(id: str):
    """Удалить продукт по id"""
    global _products
    _products = [p for p in _products if p.id != id]


def get_by_id(id: str) -> Optional[Product]:
    """Просмотреть продукт по id"""
    return next((p for p in _products if p.id == id), None)


def get_many(page: int = 0, limit: int = 10):
    """Просмотреть список продуктов"""
    start = page * limit
    end = start + limit
    return _products[start:end]
