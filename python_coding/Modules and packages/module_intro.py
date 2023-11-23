# we can use this funciton in python interpretor by doing import module_intro
# then we can access the functions which are present in module_intro file


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()
