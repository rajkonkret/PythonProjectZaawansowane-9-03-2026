from typing import Any

print('Kilka przykładów funkcji')


def witaj(imie: str) -> str:
    return f'Miło Cię widzieć {imie}'


def konkurs(imie: str, punkty: int, miejsce: int) -> str:
    return f"Uczestnik konkursu {imie}, liczba punktów: {punkty}, zajęte miejsce: {miejsce}"


def bonus(punkty: int, bonus: float) -> float:
    return punkty * bonus


def osoba(funkcja: Any, *args) -> Any:
    return funkcja(*args)


print(osoba(witaj, 'Leon'))  # Miło Cię widzieć Leon
print(osoba(konkurs, 'Anna', 78, 9))
print(osoba(bonus, 66, 0.2))


# Kilka przykładów funkcji
# Miło Cię widzieć Leon
# Uczestnik konkursu Anna, liczba punktów: 78, zajęte miejsce: 9
# 13.200000000000001

# prosty dekorator
def startstop(funkcja):
    def wrapper(*args, **kwargs):
        print(60 * "_")
        print("startowanie procesu...")
        funkcja(*args, **kwargs)
        print("kończenie procesu...")

    return wrapper  # zwroci adres


def zawijanie(w_co):
    print(f'Zawijanie czekoladek w {w_co}')


zw = startstop(zawijanie)

print(zw)
# <function startstop.<locals>.wrapper at 0x000002B341109900>
print(type(zw))  # <class 'function'>

zw("sreberka")


# startowanie procesu...
# Zawijanie czekoladek w sreberka
# kończenie procesu...

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodziny")


dmuchanie("baloników")
dmuchanie('swieczek na torcie')

# ____________________________________________________________
# startowanie procesu...
# dmuchanie baloników na urodziny
# kończenie procesu...
# ____________________________________________________________
# startowanie procesu...
# dmuchanie swieczek na torcie na urodziny
# kończenie procesu...
