import math
import sys

from joblib import Parallel, delayed

sys.set_int_max_str_digits(1_000_000)


def compute_factorial(n):
    print(f"Obliczenia silnii {n}")
    return math.factorial(n)


numbers = [5, 7, 19, 112, 180, 260, 400, 10000]

# result = Parallel(n_jobs=4)(delayed(compute_factorial)(n) for n in numbers)
result = Parallel(n_jobs=-1)(delayed(compute_factorial)(n) for n in numbers)  # n_jobs=-1 wszystkie dostepne rdzenie CPU
print(f"Wyniki silnia: {result}")
