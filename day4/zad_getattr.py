class SecureData:
    def __init__(self, public, secret):
        self.public = public
        self._secret = secret

    @property
    def info(self):
        return f"PUBLIC={self.public}"

    def hello(self):
        return "hello"

    def __getattribute__(self, name):
        print(f"[LOG] Próba dostępu do atrybutu: {name}")

        if name == "_secret":
            raise AttributeError("Brak dostępu do _secret")

        return super().__getattribute__(name)


print("=== Tworzenie obiektu ===")
obj = SecureData("widoczne dane", "tajne dane")

print("\n=== 1. Normalny atrybut ===")
print(obj.public)

print("\n=== 2. Property ===")
print(obj.info)

print("\n=== 3. Metoda ===")
print(obj.hello())

print("\n=== 4. Zablokowany sekret ===")
try:
    print(obj._secret)
except AttributeError as e:
    print("Błąd:", e)

print("\n=== 5. hasattr ===")
print(hasattr(obj, "_secret"))

print("\n=== 6. Obejście blokady ===")
print(object.__getattribute__(obj, "_secret"))

print("\n=== 7. __dict__ ===")
print(obj.__dict__)