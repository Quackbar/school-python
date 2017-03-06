# -----------------------------------------+
# Sam Luther                		   |
# pascasl.py                               |
# Last Updated: January 9, 2016            |  
# -----------------------------------------|
# It is a program                          |  
# -----------------------------------------+

def combination(n, k):
    valueToReturn = 0
    if(k==0 or k == n):
        return "1"
    else:
        valueToReturn = valueToReturn + int(combination(n-1,k-1)) + int(combination(n-1,k))
    return valueToReturn

def pascals_triangle(rows):
    for row in range(rows):
        answer = ""
        for column in range(row + 1):
            answer = answer + str(combination(row, column)) + "\t"
        print(answer)
while(True):
    entered = int(input("Input a number to enter paskals triangle: "))
    pascals_triangle(entered)
