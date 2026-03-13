import sys


class Normal:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Slotted:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


n = Normal(1, 2)
s = Slotted(1, 2)

print("Normal na __dict__:", hasattr(n, "__dict__"))
print("Slotted na __dict__:", hasattr(s, "__dict__"))

# n.z = 9999
# print("Normal.z=", n.z)  # Normal.z= 9999
#
# try:
#     s.z = 999
# except AttributeError as e:
#     print("Slotted: bład przy s.z=", e)
#     # Slotted: bład przy s.z= 'Slotted' object has no attribute 'z' and no __dict__ for setting new attributes

# wielkosc
print("Rozmiar Normal", sys.getsizeof(n))
print("Rozmiar Slotted", sys.getsizeof(s))
# Rozmiar Normal 48
# Rozmiar Slotted 48
