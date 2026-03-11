import time
import operator
from functools_ex import partial

import numpy as np


def pomiarczasu(funkcja):
    def wrapper():
        start_time = time.time()
        funkcja()
        end_time = time.time()
        wynik = end_time - start_time
        print(f"Czas wykonania funkcji {funkcja.__name__}: {wynik} s")

    return wrapper


@pomiarczasu
def my_wait():
    time.sleep(2)


@pomiarczasu
def my_for_sum():
    total = 0
    for i in range(15_000_000):
        total += i
    print("sum is:", total)


@pomiarczasu
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("sum is:", total)


@pomiarczasu
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


my_wait()  # Czas wykonania funkcji: 2.00087308883667 s
my_for_sum()
my_sum_without_for()
my_sum_np()
# Czas wykonania funkcji: 2.0006773471832275 s
# sum is: 112499992500000
# Czas wykonania funkcji: 0.7210917472839355 s
# sum is: 112499992500000
# Czas wykonania funkcji: 0.2207622528076172 s
# Sum is: 112499992500000
# Czas wykonania funkcji: 0.050234079360961914 s

print("-----")
lista = list(range(1_000_000))


@pomiarczasu
def my_for_mul():
    l = []
    for i in lista:
        l.append(i * 2)


funkcja = lambda x: x * 2


@pomiarczasu
def my_for_with_map_mul():
    l_map = list(map(funkcja, lista))


@pomiarczasu
def my_for_list_c():
    l = [i * 2 for i in lista]


@pomiarczasu
def my_for_with_map_operator():
    l_map = list(map(partial(operator.mul, 2), lista))


my_for_mul()
my_for_with_map_mul()
my_for_list_c()
my_for_with_map_operator()
# Czas wykonania funkcji my_for_mul: 0.1123194694519043 s
# Czas wykonania funkcji my_for_with_map_mul: 0.15184879302978516 s
# Czas wykonania funkcji my_for_list_c: 0.10686707496643066 s
# Czas wykonania funkcji my_for_mul: 0.08449339866638184 s
# Czas wykonania funkcji my_for_with_map_mul: 0.12586045265197754 s
# Czas wykonania funkcji my_for_list_c: 0.07619166374206543 s
# Czas wykonania funkcji my_for_with_map_operator: 0.08768177032470703 s


zm = (i * 2 for i in range(10))  # <class 'generator'>
print(type(zm))
