##Sam Luther
##Eras.py
##12/7/16

year = float(input('How many million years ago was it: '))

while(year>0):
    if(year<=66):
        print('This year was in the Mesozoic era.')
    elif(year>66 and year<=252.17):
        print('This year was in the Cenezoic era.')
    else:
        print('This years era is unknown.')
    year=-1
