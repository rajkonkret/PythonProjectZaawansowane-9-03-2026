from functools import wraps
import inspect


def decor_no_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decor_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decor_no_wraps
def add(a: int, b: int) -> int:
    """Dodawanie dwie liczby"""
    return a + b


@decor_with_wraps
def mul(a: int, b: int) -> int:
    """Mnoży dwie liczby"""
    return a * b


print("=== Bez @wraps ===")
print("name:", add.__name__)
print("qualname:", add.__qualname__)
print("doc:", add.__doc__)
print("annotations:", add.__annotations__)
print("signature:", inspect.signature(add))
print("has __wrapped__:", hasattr(add, "__wrapped__"))
print()

print("=== Z @wraps ===")
print("name:", mul.__name__)
print("qualname:", mul.__qualname__)
print("doc:", mul.__doc__)
print("annotations:", mul.__annotations__)
print("signature:", inspect.signature(mul))
print("has __wrapped__:", hasattr(mul, "__wrapped__"))
print()

# === Bez @wraps ===
# name: wrapper
# qualname: decor_no_wraps.<locals>.wrapper
# doc: None
# annotations: {}
# signature: (*args, **kwargs)
# has __wrapped__: False
#
# === Z @wraps ===
# name: mul
# qualname: mul
# doc: Mnoży dwie liczby
# annotations: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
# signature: (a: int, b: int) -> int
# has __wrapped__: True