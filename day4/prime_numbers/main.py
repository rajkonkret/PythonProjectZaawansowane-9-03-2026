import time
import concurrent.futures

from funkcja_prime import find_the_sum_prime_nums

numbers = [(1, 10_000), (3, 50_000), (5_000, 100_000), (4, 9000), (8_000, 15_000), (95_000, 133_000), (200, 67_340)]


def synchronicznie():
    starttime = time.time()
    for pair in numbers:
        st = time.time()
        prime_suma = find_the_sum_prime_nums(*pair)
        et = time.time()
        print(f"Wynik = {prime_suma}, czas wykonania: {et - st} s")
    endtime = time.time()

    print(f"Całkowity czas wykonania wszystkich sum (synchronicznie): {endtime - starttime}")


def run_heavt_function(params):
    return find_the_sum_prime_nums(*params)


def asymchronicznie():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        result = executor.map(run_heavt_function, numbers)
    end_time = time.time()
    print(f"Całkowity czas wykonania wszystkich sum (asynchronicznie): {end_time - start_time}")


def main():
    synchronicznie()
    asymchronicznie()


if __name__ == '__main__':
    main()
# Wynik = None, czas wykonania: 0.1360936164855957 s
# Wynik = None, czas wykonania: 2.896277666091919 s
# Wynik = None, czas wykonania: 11.040292978286743 s
# Wynik = None, czas wykonania: 0.1107187271118164 s
# Wynik = None, czas wykonania: 0.20446014404296875 s
# Wynik = None, czas wykonania: 9.070082187652588 s
# Wynik = None, czas wykonania: 5.185152292251587 s
# Całkowity czas wykonania wszystkich sum (synchronicznie): 28.64328932762146
# Całkowity czas wykonania wszystkich sum (asynchronicznie): 13.506874561309814
