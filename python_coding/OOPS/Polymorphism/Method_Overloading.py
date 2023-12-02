# Method overloading is the overloadin the certain method
# example: __add__(self,other)
# the above method will take the certian number of arguments and types of arguments
# If we want we can overload them by changing the number of arguments or type of arguments

class Overloading:
    def __init__(self) -> None:
        pass

    # In python we can overload directly by declaring the another method
    # with the same name sum
    # we do some trick like default values
    def sum(self, a=None, b=None, c=None):
        s = 0

        if a != None and b != None and c != None:  # if we are passing all three arguments
            s = a+b+c
        elif a != None and b != None:  # if we are passing only two arguments
            s = a+b
        else:  # if we are passing only one arguments
            s = a

        return s

cal = Overloading()

print(cal.sum(2,3,4))
print(cal.sum(4,5))
print(cal.sum(5))