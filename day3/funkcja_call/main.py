"""
Trzy przypadki użycia funkcji __call__
1. Licznik wywołań funkcji
2. Walidacja danych wejsciowych
3. implementacja cache
"""

from counter_zad1 import CallCounter
from validator import RangeValidator
from cache import CacheFunction

print(70 * "-")
counter = CallCounter()
counter()
counter()
counter()
counter()
counter()

# ----------------------------------------------------------------------
# funkcję call wywołano 1 razy
# funkcję call wywołano 2 razy
# funkcję call wywołano 3 razy
# funkcję call wywołano 4 razy
# funkcję call wywołano 5 razy

print(70 * "-")
valid = RangeValidator(2, 20)
valid(3)
valid(17)
valid(8)
valid(44)

print(70 * "-")


def efunction(x, y):
    return x ** y + y ** x


ce_func = CacheFunction(efunction)
print(ce_func(2, 3))
print(ce_func(2, 3))
print(ce_func(2, 3))
print(ce_func(2, 3))
print(ce_func(2, 3))
print(ce_func(12, 1))
print(ce_func(12, 1))
print(ce_func(2, 3))
# ----------------------------------------------------------------------
# wynik obliczeń dla argumentów: (2, 3)
# 17
# wynik w cache dla argumentów: (2, 3)
# 17
# wynik w cache dla argumentów: (2, 3)
# 17
# wynik w cache dla argumentów: (2, 3)
# 17
# wynik w cache dla argumentów: (2, 3)
# 17
# wynik obliczeń dla argumentów: (12, 1)
# 13
# wynik w cache dla argumentów: (12, 1)
# 13
# wynik w cache dla argumentów: (2, 3)
# 17
