import threading


def worker(num, shared_variable):
    shared_variable.append(num)
    print(f"Wątek {threading.current_thread()} dodał {num} do zmiennej współdzielonej")


shared_variable = []
threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i, shared_variable))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Zmienna współdzielona po zakończeniu pracy wątków: {shared_variable}")
# Wątek <Thread(Thread-1 (worker), started 5548)> dodał 0 do zmiennej współdzielonej
# Wątek <Thread(Thread-2 (worker), started 17128)> dodał 1 do zmiennej współdzielonej
# Wątek <Thread(Thread-3 (worker), started 16896)> dodał 2 do zmiennej współdzielonej
# Wątek <Thread(Thread-4 (worker), started 17860)> dodał 3 do zmiennej współdzielonej
# Wątek <Thread(Thread-5 (worker), started 1424)> dodał 4 do zmiennej współdzielonej
# Zmienna współdzielona po zakończeniu pracy wątków: [0, 1, 2, 3, 4]
