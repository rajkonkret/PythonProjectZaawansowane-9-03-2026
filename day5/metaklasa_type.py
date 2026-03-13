class MojaMeta(type):
    def __new__(cls, clsname, superclasses, attrs):
        print(f"_____ {cls.__class__.__name__} ________")
        print(f"Nazwa klasy: {clsname}")
        print(f"Klasa dziedziczona: {superclasses}")
        print(f"Słownik atrybutów klasy: {attrs}")
        return type.__new__(cls, clsname, superclasses, attrs)

    def jedynka(cls):
        return 1


class S:
    pass


class F:
    pass


class Specjalna(S, metaclass=MojaMeta):
    pass


class B(Specjalna):
    pass


class C(F, B):

    @property
    def info(self):
        print("abc...")


class D(F):
    pass


obiekt_c = C()
# print(obiekt_c.jedynka())
# AttributeError: 'C' object has no attribute 'jedynka'
klasa_c = C
print(type(obiekt_c))
print(type(klasa_c))
# _____ type ________
# Nazwa klasy: Specjalna
# Klasa dziedziczona: (<class '__main__.S'>,)
# Słownik atrybutów klasy: {'__module__': '__main__', '__qualname__': 'Specjalna', '__firstlineno__': 21, '__static_attributes__': ()}
# _____ type ________
# Nazwa klasy: B
# Klasa dziedziczona: (<class '__main__.Specjalna'>,)
# Słownik atrybutów klasy: {'__module__': '__main__', '__qualname__': 'B', '__firstlineno__': 25, '__static_attributes__': ()}
# _____ type ________
# Nazwa klasy: C
# Klasa dziedziczona: (<class '__main__.F'>, <class '__main__.B'>)
# Słownik atrybutów klasy: {'__module__': '__main__', '__qualname__': 'C', '__firstlineno__': 29, 'info': <property object at 0x000001774D0D58F0>, '__static_attributes__': (), '__classdictcell__': <cell at 0x0000017757AD52D0: dict object at 0x000001774CC38880>}
# <class '__main__.C'>
# <class '__main__.MojaMeta'>

print(klasa_c.jedynka())  # 1
