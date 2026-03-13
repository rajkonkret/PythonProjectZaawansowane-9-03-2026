import time
import concurrent.futures
import multiprocessing
import os

from funkcja_prime import find_the_sum_prime_nums

numbers = [(1, 10_000), (3, 50_000), (5_000, 100_000), (4, 9000), (8_000, 15_000), (95_000, 133_000), (200, 67_340)]


def multi():
    starttime = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(run_heavt_function, numbers)
    end_time = time.time()
    print(f"Całkowity czas wykonania wszystkich sum (multi process): {end_time - starttime}")


def run_heavt_function(params):
    return find_the_sum_prime_nums(*params)


def asymchronicznie():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        result = executor.map(run_heavt_function, numbers)
    end_time = time.time()
    print(f"Całkowity czas wykonania wszystkich sum (asynchronicznie): {end_time - start_time}")


def main():
    multi()
    asymchronicznie()


if __name__ == '__main__':
    main()
# Całkowity czas wykonania wszystkich sum (multi process): 12.02274775505066
# Całkowity czas wykonania wszystkich sum (asynchronicznie): 12.259918212890625
