class debug:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*a, **kw):
            print(f"[{self.name}] calling {func.__name__}")
            return func(*a, **kw)
        return wrapper

@debug("TEST")
def f(x):
    return x + 1

print(f(4))