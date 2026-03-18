from functools import wraps


def cache_results(func):
    cache = {}
    print("ID cache:", id(cache))

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Używam cache o ID:", id(cache))
        ...
    return wrapper

def outer():
    x = []

    def inner(value):
        x.append(value)
        print(x)

    return inner

f = outer()
f(1)
f(2)
f(3)

from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args
        if key in cache:
            print(f"[CACHE {func.__name__}] {key} -> {cache[key]}")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"[NEW {func.__name__}] {key} -> {result}")
        return result

    return wrapper


@cache_results
def f(x):
    return x + 1


@cache_results
def g(x):
    return x * 2