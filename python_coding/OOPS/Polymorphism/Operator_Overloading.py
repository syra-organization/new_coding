# Operator overloading is overloading the existing properties

class Student:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    # overloading the __add__ for this class becuase of s3 below

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    # Overloading __str__ for print the values of class below

    def __str__(self):
        # formating this becuase it should return the string

        return '{}'.format({"m1": self.m1, "m2": self.m2})

    # overloading __gt__(greater than) becuase of below conditional statement

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False


# Student 1
s1 = Student(71, 40)

# Student 2
s2 = Student(60, 50)

# Student 3

s3 = s1 + s2

# Initialy this will print address
print(s1)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
