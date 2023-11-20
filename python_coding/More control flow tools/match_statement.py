# match is like a switch case in js

# example status

# status = int(input("Enter status value: "))

# match status:
#     case 400:
#         print('Bad request')
#     case 404:
#         print('Not found')
#     case _:
#         print('Something went wrong')

# points example using tuple

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

point = (x, y)

match point:
    case (0, 0):
        print('Origin')
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        print('not origin')
