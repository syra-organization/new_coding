a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))


def div(a, b):
    print(a//b)

# Decorators


def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
            print(a, b)
        return func(a, b)
    return inner


new_div = smart_div(div)

new_div(a, b)
