from pydantic import BaseModel, ValidationError, field_validator

class Product(BaseModel, validate_assignment=True):
    name: str
    price: float
    stock: int

    @field_validator("price")
    @classmethod
    def price_positive(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("price musi być > 0")
        return value

try:
    p = Product(name="Laptop", price=4999.99, stock=10)
    print(p)

    p.stock = 20      # OK
    p.price = -1      # ValidationError
except ValidationError as e:
    print(e)