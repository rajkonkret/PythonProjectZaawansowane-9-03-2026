from funcwraps import dekorator
from cache import fibonacci
from oblicznie import podwojenie


def main():
    print("Przykład uzycia dekoratora z @wraps")

    @dekorator
    def wrap_przyklad():
        return 'prosta funkcja'

    print(wrap_przyklad())

    print('Przykład użycia lru_cache')
    print(fibonacci(10))
    print(fibonacci.cache_info())
    # CacheInfo(hits=8, misses=11, maxsize=128, currsize=11)
    fibonacci.cache_clear()
    print(fibonacci.cache_info())
    # CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)

    print("przykład użycia  ** partial **")
    print(podwojenie(5))  # 10


if __name__ == '__main__':
    main()
# Przykład uzycia dekoratora z @wraps
# informacja:abc
# Zakończenie
# prosta funkcja

# Przykład użycia lru_cache
# 55
