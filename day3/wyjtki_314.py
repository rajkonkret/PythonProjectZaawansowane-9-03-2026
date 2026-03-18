
# nie dziąl w 314
def h(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return None
    finally:
        return 123  # zły pomysł
    # SyntaxWarning: 'return' in a 'finally' block

    # bezpieczne dla 314:
    def h(x):
        try:
            result = 10 / x
        except ZeroDivisionError:
            result = None
        finally:
            print("sprzątanie")
        return result