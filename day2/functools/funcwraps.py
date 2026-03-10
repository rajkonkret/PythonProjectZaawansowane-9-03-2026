from functools import wraps


def dekorator(funkcja):
    @wraps(funkcja)
    def wrapper(*args, **kwargs):
        print("informacja:abc")
        wynik = funkcja(*args, **kwargs)
        print('Zakończenie')
        return wynik

    return wrapper
