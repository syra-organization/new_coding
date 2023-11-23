class Animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f'{self.name} says wook!'

class Cat(Animal):
    def speak(self):
        return f'{self.name} says foo!'
    
x = Dog('rocky')

print(x.name)

