# tuple is immutable

tup = (1, 2, 3, 4, 5)
print(tup)  # (1,2,3,4,5)

print(tup[1])  # 2

# We cannot change the value inside the tuple

# example

tup[1] = 10  # you will get an erro called "tuple object does not support item assignment"
print(tup)
