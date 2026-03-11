class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


class Myvalidator:

    @staticmethod
    def is_int(value, name):
        if not isinstance(value, int):
            raise MyTypeError(f"{name} must be integer")

    @staticmethod
    def not_zero(value, name):
        if value == 0:
            raise MyValueError(f'{name} cannot be zero')


def my_function(x: int, y: int) -> float:
    Myvalidator.is_int(x, "x")
    Myvalidator.is_int(y, "y")
    Myvalidator.not_zero(y, "y")


try:
    my_function(1, 2)
    my_function(1, '2')
except MyTypeError as e:
    print("Bład:", e)
# Bład: y must be integer
