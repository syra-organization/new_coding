# Example

class NewClass:
    i = 10

    def foo(self):
        return 'Hello world'


x = NewClass()

print(x.foo())

# init method


class Complex:
    def __init__(self, realpart, imagepart) -> None:
        self.r = realpart
        self.i = imagepart


cl = Complex(1, 2)

tup = (cl.r, cl.i)

print(tup)

# instance variable and class variable


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

# Private variable


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method
