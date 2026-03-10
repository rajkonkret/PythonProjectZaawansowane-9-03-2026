import time


def pomiarczasu(funkcja):
    def wrapper():
        start_time = time.time()
        funkcja()
        end_time = time.time()
        wynik = end_time - start_time
        print(f"Czas wykonania funkcji: {wynik} s")

    return wrapper


def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()

    return wrapper


@pomiarczasu
@usypiacz
def big_lista():
    sum([i ** 5 for i in range(10_000_000)])


big_lista()


# Czas wykonania funkcji: 5.314753770828247 s

def debug(funkcja):
    def wrapper(*args):
        print(f"Wołana funkcja: {funkcja.__name__}")
        funkcja(*args)

    return wrapper


@debug
def info(i):
    print(f'Ważny kod: {i}')


info("65432178900")


# Wołana funkcja: info
# Ważny kod: 65432178900

def sprawdz_typy(typy):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            for (arg, typ) in zip(args, typy):
                if not isinstance(arg, typ):
                    raise TypeError(f'Argument: {arg} nie jest typu: {typ}')
            return funkcja(*args, **kwargs)

        return wrapper

    return dekorator


@sprawdz_typy((int, int))
def mnozenie(a, b):
    return a * b


try:
    print(mnozenie(6, 8))
    print(mnozenie(6, "osiem"))
except TypeError as te:
    print(te)  # 48


# Argument: osiem nie jest typu: <class 'int'>

def memoizacja(funkcja):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Zwracanie wyniku z ache dla argumentów {args}")
            print(f"funkcja: {funkcja.__name__}({args} -> {funkcja(*args)})")
            return cache[args]
        else:
            wynik = funkcja(*args)
            cache[args] = wynik
            return wynik

    return wrapper


@memoizacja
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
# Zwracanie wyniku z ache dla argumentów (1,)
# funkcja: fibonacci((1,) -> 1)
# Zwracanie wyniku z ache dla argumentów (0,)
# funkcja: fibonacci((0,) -> 0)
# funkcja: fibonacci((2,) -> 1)
# Zwracanie wyniku z ache dla argumentów (1,)
# funkcja: fibonacci((1,) -> 1)
# funkcja: fibonacci((3,) -> 2)
# Zwracanie wyniku z ache dla argumentów (2,)
# Zwracanie wyniku z ache dla argumentów (1,)
# funkcja: fibonacci((1,) -> 1)
# Zwracanie wyniku z ache dla argumentów (0,)
# funkcja: fibonacci((0,) -> 0)
# funkcja: fibonacci((2,) -> 1)
# funkcja: fibonacci((4,) -> 3)
# funkcja: fibonacci((6,) -> 8)
# funkcja: fibonacci((8,) -> 21)
# 55
