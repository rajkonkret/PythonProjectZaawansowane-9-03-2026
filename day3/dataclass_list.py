from dataclasses import dataclass, field
from typing import List
import datetime


@dataclass
class Order:
    customer: str
    items: List[int] = field(default_factory=list)
    items_d: List[int] = field(default_factory=lambda: ["A", "B", "C"])
    order_state: datetime.datetime = field(default_factory=datetime.now)
    status: str = "Pending"
