from dataclasses import dataclass

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
print(p.__dict__)  # {'nazwa': 'pudełko', '_licznik': 56, 'cena': 11.45}
