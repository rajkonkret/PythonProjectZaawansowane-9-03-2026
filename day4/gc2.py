import gc

class Box:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __del__(self):
        print(f"USUWAM obiekt: {self.name}")


print("=== TWORZENIE ===")
a = Box("A")
b = Box("B")

a.ref = b
b.ref = a

print("a.ref.name =", a.ref.name)
print("b.ref.name =", b.ref.name)

print("\n=== USUWAM ZEWNĘTRZNE REFERENCJE ===")
a = None
b = None

print("Po a=None i b=None")
print("Obiekty nadal mogą istnieć przez cykl referencji.")

print("\n=== RĘCZNE SPRZĄTANIE ===")
unreachable = gc.collect()
print("gc.collect() znalazł obiektów do posprzątania:", unreachable)

print("=== KONIEC ===")