year = int(input('Please input a year to check for leap year: '))

def yearCheck(year):
    if(year%4 == 0):
        if(year%100 == 0):
            if(year%400 == 0):
                print(str(year)+' is a leap year.')
            else:
                print(str(year)+' is not a leap year.')
        else:
            print(str(year)+' is a leap year.')
    else:
        print(str(year)+' is not a leap year.')

yearCheck(year)
print(len(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'))
