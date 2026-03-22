import sys


GLOBAL_VALUE = "jestem globalem"


def outer(x: int) -> int:
    outer_local = "zmienna z outer"

    def inner(y: int) -> int:
        inner_local = "zmienna z inner"

        frame = sys._getframe()

        print("=== FRAME inner ===")
        print("Nazwa funkcji:", frame.f_code.co_name)
        print("Zmienne lokalne:", frame.f_locals)
        print("Nazwa pliku:", frame.f_code.co_filename)

        print("\n=== FRAME caller (outer) ===")
        caller = frame.f_back
        print("Nazwa funkcji:", caller.f_code.co_name)
        print("Zmienne lokalne:", caller.f_locals)

        return x + y

    return inner(5)


print(outer(10))

class User:
    def say_hello(self) -> str:
        return "Cześć!"


u = User()

print(User.__dict__["say_hello"])
print(u.say_hello)
print(u.say_hello())

def greet(name: str) -> str:
    return f"Cześć {name}"

print("=== Funkcja greet ===")
print(type(greet))
print(id(greet))
print(greet.__name__)
print(greet.__module__)
print(greet.__dict__)


# print

def greet(name: str) -> str:
    return f"Cześć {name}"

greet.category = "utility"

print(greet.__dict__)
print(greet.category)
