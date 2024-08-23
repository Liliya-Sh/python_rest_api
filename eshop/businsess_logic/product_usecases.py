from typing import Optional, List

from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import save, get_by_id, get_many, _products


def product_create(name: str, price: float) -> Product:
    """Создаем продукт"""
    for product in _products:
        if product.name == name:
            raise ValueError("Продукт с таким именем уже существует.")

    product = Product(id=len(_products) + 1, name=name, price=price)
    save(product)
    return product


def product_get_many(page: int, limit: int) -> List[Product]:
    """Просмотреть список продуктов"""
    return get_many(page=page, limit=limit)
