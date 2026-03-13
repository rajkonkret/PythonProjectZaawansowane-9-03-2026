import concurrent.futures
import time


def task(n):
    print(f"start zadania {n}")
    time.sleep(2)
    print(f"Koniec zdarzenia {n}")

    return n * 2


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

    print(f"wynik: {results}")
# start zadania 0
# start zadania 1m
# start zadania 2
# start zadania 3
# Koniec zdarzenia 0
# start zadania 4
# Koniec zdarzenia 2
# Koniec zdarzenia 3
# Koniec zdarzenia 1
# Koniec zdarzenia 4
# wynik: [0, 4, 6, 2, 8]