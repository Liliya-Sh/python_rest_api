from dataclasses import dataclass
from typing import List


@dataclass
class Order:
    id: str
    product_ids: List[str]
    total: int
