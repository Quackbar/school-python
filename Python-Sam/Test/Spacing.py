name = str(input("Please enter your name: "))
length = int(input("Enter the field width: "))
halfL = length/2
space2 = ''
while(halfL!=0):
    space2 = (''+space2+' ')
    halfL = halfL - 1
print('+'+space2+name+space2+'+')


##firstName.center(fieldWidth)
