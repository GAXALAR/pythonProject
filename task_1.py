class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class MyClass1:
    name = Descriptor('name')
    age = Descriptor('age')

class MyClass2:
    city = Descriptor('city')
    country = Descriptor('country')