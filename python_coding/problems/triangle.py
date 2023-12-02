side1 = int(input('Enter side one value: '))
side2 = int(input('Enter side two value: '))
side3 = int(input('Enter side three value: '))

if side1 == side2 and side1 == side3:
    print('Triangle is equilatral')
elif side1 == side2 and side1 != side3 or side1 == side3 and side1 != side2 or side2 == side3 and side2 != side1:
    print('Triangle is isosceles')
elif side1 != side2 and side1 != side3:
    print('Triagle is scalene')