x = int(input('Enter x value: '))
y = int(input('Enter y value: '))

if x > 0 and y > 0:
    print('x , y lies in first coordinate')
elif x < 0 and y > 0:
    print('x , y lies in second coordinate')
elif x < 0 and y < 0:
    print('x , y lies in third coordinate')
else:
    print('x , y lies in fourth coordinate')