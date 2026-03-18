class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Person:
    age = Descriptor()
    height = Descriptor()

p = Person()
p.age = 30
p.height = 180

print(p.age)     # 30
print(p.height)  # 180