from functools import reduce

arr = [1, 2, 3, 4, 5]

sum = reduce(lambda a, v: a+v, arr)

print(sum)
