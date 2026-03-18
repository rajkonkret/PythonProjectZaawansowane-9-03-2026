import gc
from weakref import WeakKeyDictionary


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({self.name!r})"

    def __del__(self):
        print(f"USUWAM obiekt: {self.name}")


def normal_dict_example():
    print("\n=== Zwykły dict ===")
    d = {}

    u = User("Jan")
    d[u] = "dane Jana"

    print("Przed usunięciem zmiennej u:")
    print(d)

    u = None
    gc.collect()

    print("Po u = None i gc.collect():")
    print(d)
    print("Obiekt nadal żyje, bo dict trzyma go jako klucz.")


def weak_dict_example():
    print("\n=== WeakKeyDictionary ===")
    d = WeakKeyDictionary()

    u = User("Adam")
    d[u] = "dane Adama"

    print("Przed usunięciem zmiennej u:")
    print(dict(d))

    u = None
    gc.collect()

    print("Po u = None i gc.collect():")
    print(dict(d))
    print("Wpis znika, bo WeakKeyDictionary nie trzyma klucza przy życiu.")


normal_dict_example()
weak_dict_example()