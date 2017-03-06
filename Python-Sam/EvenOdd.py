##Sam Luther
##EvenOdd: It tells you whether or not a inputed number is even
##11/3/16


n=float(input("Please input a number to see if it is even:"))

def is_odd(n):
    c = float(n%2)
    if(c==0):
        print(str(n)+' is an even number.')
    if(c!=0):
        print(str(n)+' is not an even number.')
is_odd(n)
        
