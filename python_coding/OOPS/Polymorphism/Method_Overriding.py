# Methong overriding is simply a override the properties of some method

class A:
    def __init__(self) -> None:
        pass

    def show(self):
        print('Showing A')

class B(A):
    def __init__(self) -> None:
        pass

    # I override the properties of class "A" and method "show" using inheritance

    def show(self):
        print('showing B')

cls = B()
cls.show()