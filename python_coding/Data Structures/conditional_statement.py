x = int(input("Please enter an integer: "))

# "IF" condition

if x < 0:
    print('number is less than zero')
elif x > 0 and x % 2 == 0:
    print('number is grethan than zero and it is event number')
elif x == 0:
    print('number is zero')
else:
    print('number is not zero')
