class Osoba:
    def __init__(self, imie, nazwisko, wiek, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.waga = waga
        self.wzost = wzrost

    def get_waga(self):
        return self.waga

    def set_waga(self, nowa_waga):
        self.waga = nowa_waga

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        self._wiek = nowy_wiek

    @property
    def bmi(self):
        return self.waga / (self.wzost / 100) ** 2


os = Osoba("Jan", 'Kos', 30, 89, 176)
print(os)
print(os.get_waga())
os.set_waga(98)
print(os.get_waga())
# 89
# 98

print(os.wiek)  # 30
os.wiek = 38
print(os.wiek)  # 38

os.waga = 87
os.wzost = 193

print(f"{os.bmi: 2f}")
#  23.356332
