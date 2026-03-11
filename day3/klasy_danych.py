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


@dataclass
class Dane:
    nazwa: str
    licznik: int
    cena: float = 10.00

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self, me):
        self._licznik = me


p = Dane("pudełko", 4, 11.45)
# p = Dane("pudełko", 11.45)
print(p)
# Dane(nazwa='pudełko', licznik=4, cena=11.45)
print(p.licznik)
p.licznik = 56
print(p)
# Dane(nazwa='pudełko', licznik=56, cena=11.45)
print(p.__dict__) # {'nazwa': 'pudełko', '_licznik': 56, 'cena': 11.45}