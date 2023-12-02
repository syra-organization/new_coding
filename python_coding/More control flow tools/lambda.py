# small anonymous funcitons can be created with the lambda function

def make_sum(a, b):
    return lambda a, b: a + b


f = make_sum(0, 0)

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))

print(f(a,b))