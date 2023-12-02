# Abstract class is class which should atleast contains one abstrct method
# Abstrct method is a method where it doesn't have any code to execute

# Certainly! In Python, an abstract class is a class that cannot be instantiated directly. It serves as a blueprint for other classes and may contain abstract methods, which are methods that have no implementation in the abstract class itself but must be implemented by concrete (sub)classes that inherit from it.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):  # Abstract class
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    @abstractmethod
    def area(self):  # abstract method
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, name, side) -> None:
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


c1 = Circle('Circle', 4)
s1 = Square('Square', 5)

print(f'Area of {c1.name} is {c1.area()}')
print(f'Perimeter of {c1.name} is {c1.perimeter()}')
print(f'Area of {s1.name} is {s1.area()}')
print(f'Perimeter of {s1.name} is {s1.perimeter()}')
