from dataclasses import dataclass


class Liczba:
    def __init__(self, x, y):
        self.x = x
        self.y = y


liczba = Liczba(5, 3)
print(liczba)  # <__main__.Liczba object at 0x00000211AE960AD0>
print(liczba.x)
print(liczba.y)


@dataclass()
class DLiczba:
    x: int
    y: int
    z: float


dl = DLiczba(5, 3, 4.6)
print(dl.z)

print(dl)  # DLiczba(x=5, y=3, z=4.6)


