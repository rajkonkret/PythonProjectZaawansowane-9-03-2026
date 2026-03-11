"""
Trzy przypadki użycia funkcji __call__
1. Licznik wywołań funkcji
2. Walidacja danych wejsciowych
3. implementacja cache
"""

from counter_zad1 import CallCounter

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