class ContexManager:
    def __init__(self):
        print("Inicjacja metody __init__()")

    def __enter__(self):
        # print(5 / 0)
        print("Inicjacja metody __enter__()")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Inicjacja metody __exit__()")


with ContexManager() as manager:
    print("Działanie wewnatrz instrukcji with...")
# Inicjacja metody __init__()
# Inicjacja metody __enter__()
# Działanie wewnatrz instrukcji with...
# Inicjacja metody __exit__()
