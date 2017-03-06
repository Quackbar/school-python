##Sam Luther
##printNumberRecursion
##12/20/16

def printNumbers(beginNumber):
    print()
    for i in range(beginNumber,0,-1):
        print(str(i)+"\t",end='')
    if(beginNumber - 1 >= 0):
        printNumbers(beginNumber-1)    

bNumber = int(input('Input a number:'))
printNumbers(bNumber)


    
