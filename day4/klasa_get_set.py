from weakref import WeakKeyDictionary


class LoggedPositiveInt:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        print(f"{instance}")

    def __set__(self, instance, value):
        print("Ustawiasz pole")


class Product:
    stock = LoggedPositiveInt()

    def __init__(self, stock):
        self.stock = stock


p1 = Product(10)
p2 = Product(5)

print(p1.stock)
p1.stock = 20
print(p2.stock)

# 3 Ustawiasz pole
# Ustawiasz pole
# <__main__.Product object at 0x000001A6470B1940>
# None
# Ustawiasz pole
# <__main__.Product object at 0x000001A6470ADBD0>
# None

print(Product.stock)  # None
