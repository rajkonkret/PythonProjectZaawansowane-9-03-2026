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
