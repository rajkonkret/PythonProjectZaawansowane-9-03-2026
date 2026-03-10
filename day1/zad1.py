# typy proste

import sys

print()

# int
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)

# ctrl alt l - formatowanie
# ctrl / - komentarz
# print(2024 ** 47 ** 2)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit
print(2024 ** 47)
print(47 ** 2024)
print(len(str(47 ** 2024)))  # 3385

# float
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
# min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# print(5 + "5") # silne typowanie, nie zmienia typów
print(5 + 5)  # 10
print('5' + '5')  # 55

print(45 * "9")  # 999999999999999999999999999999999999999999999
print(45 * 9)  # 405
print(int(45) + int(9))

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004

# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal - ominięcie problemu błędu zaokrąglenia

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)  # 0.3

a = Decimal(0.1)
b = Decimal(0.2)
print(a + b)  # 0.3000000000000000166533453694
print(0.1, 0.2)  # 0.1 0.2
print(a, b)
# 0.1000000000000000055511151231257827021181583404541015625 0.200000000000000011102230246251565404236316680908203125

print(True)
print(False)

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("radek"))

print(True and False)  # False

print(True or False)  # True

print(True & False)  # False bitowo

# kolekcje

# lista
# dowolny typ danych
lista = list()
lista2 = []
lista = [9, 8, 8, 9, 9]
lista2 = [10, 20, 20, 20]

lista3 = lista  # kopia referencji
print(lista)  # [9, 8, 8, 9, 9]
print(lista3)  # [9, 8, 8, 9, 9]

print(id(lista))
print(id(lista3))  # 1626004967360
print(lista is lista3)  # True

lista_copy = lista.copy()
print(id(lista_copy))  # 2373784015872
print(id(lista))  # 2373780688832

# krotka
a = ()
print(a)  # ()
print(type(a))  # <class 'tuple'>
tupla = "tomek", "radek", "zenek", "marek"
print(type(tupla))
print(tupla)  # ('tomek', 'radek', 'zenek', 'marek')

a = 1,
print(a)  # (1,)
print(type(a))  # <class 'tuple'>

a = (1,)
print(a)

# tupla[0] = "Roman" # TypeError: 'tuple' object does not support item assignment
# del tupla
# print(tupla)  # NameError: name 'tupla' is not defined. Did you mean: 'tuple'?

print(sorted(tupla))  # ['marek', 'radek', 'tomek', 'zenek']

# zbior - brak duplikatow
zb = set()
print(zb)  # set()

zbior1 = {10, 15, 15, 20, 35, 45}
zbior2 = {35, 45, 45, 55, 65}

print(zbior1)
print(zbior2)
# {35, 20, 10, 45, 15}
# {65, 35, 45, 55}

print(zbior1 & zbior2)  # {35, 45}
print(zbior1.intersection(zbior2))  # {35, 45}

print(zbior1.union(zbior2))  # {65, 35, 10, 45, 15, 20, 55} odpowiednik | suma zbiorów

# słownik
# klucz wartosci
slownik = {"name": "Radek"}  # odpowiednik jsona
print(slownik['name'])  # Radek

lista = [1, 2, 6, 3, 4, 6, 5, 6, 7, 6, 8]
while 6 in lista:
    lista.remove(6)
print(lista)

print(list(dict.fromkeys(lista)))  # [1, 2, 3, 4, 5, 7, 8]

# frozenset
# rajkonkret660@gmail.com
