class Animal:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    # __slots__ = ()
    # AttributeError: 'Dog' object has no attribute 'age' and no __dict__ for setting new attributes
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


d = Dog("Burek", 5)
