class A:
    def __init__(self) -> None:
        pass

    def feature1():
        print('Feature 1 is working')

    def feature2():
        print('Feature 2 is working')


class B(A):  # child class
    def __init__(self) -> None:
        pass

    def feature3():
        print('Feature 3 is working')

    def feature4():
        print("Feature 4 is working")


a1 = A()
b1 = B()
