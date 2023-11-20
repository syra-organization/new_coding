name = str(input('Enter student name: '))
roll_number = int(input('Enter student roll number: '))
chem = int(input('Enter chemistry marks: '))
phy = int(input('Enter physics marks: '))
computer = int(input('Enter the computer marks: '))

print('student name: ', name)
print('roll no: ', roll_number)
print('chemistry marks: ', chem)
print('physics marks: ', phy)
print('computer marks: ', computer)

total = chem + phy + computer

percentage = (total/300) * 100

print('total marks: ', total)
print('percentage: ', percentage)

division = ''

if percentage >= 80:
    division = 'First'
elif percentage >= 50 and percentage < 80:
    division = 'Second'
else:
    division = 'Third'

print('Division: ', division)
