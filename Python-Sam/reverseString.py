def reverseString():
    string= str(input('A string you would like to reverse: '))
    for i in reversed(string):
        print(i,end='')
    print('')
    reverseString()
reverseString()
